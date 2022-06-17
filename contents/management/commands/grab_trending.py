from django.core.management import BaseCommand
from contents import models as content_models
from genres import models as genre_models
import tmdbsimple as tmdb


class Command(BaseCommand):
    def handle(self, *args, **options):

        tmdb.API_KEY = "cb6371d33ed68513e62d37f350992128"

        count = 0

        movie_genre_list = genre_models.Genre.objects.filter(
            media_type=genre_models.Genre.TYPE_MOVIE
        )
        tv_genre_list = genre_models.Genre.objects.filter(
            media_type=genre_models.Genre.TYPE_TV
        )

        for i in range(1, 5):
            for video in tmdb.Trending().info(page=i)["results"]:
                try:
                    content_models.Content.objects.get(pk=video["id"])
                except content_models.Content.DoesNotExist:
                    count += 1

                    if video["media_type"] == "tv":
                        try:
                            title = video["name"]
                            released = video["first_air_date"]
                            media_type = content_models.Content.TYPE_TV
                        except KeyError:
                            pass

                    elif video["media_type"] == "movie":
                        try:
                            title = video["title"]
                            released = video["release_date"]
                            media_type = content_models.Content.TYPE_MOVIE
                        except KeyError:
                            pass

                    try:
                        pk = video["id"]
                        overview = video["overview"]
                        rating = video["vote_average"]
                        poster_path = video["poster_path"]
                    except KeyError:
                        pass

                    content = content_models.Content.objects.create(
                        title=title,
                        pk=pk,
                        overview=overview,
                        rating=rating,
                        poster_path=f"https://www.themoviedb.org/t/p/w1280{poster_path}",
                        media_type=media_type,
                    )

                    if released != "":
                        content.released = released

                    content.save()

                    if "genre_ids" in video.keys():
                        genre_ids = video["genre_ids"]
                        if video["media_type"] == "tv":
                            for i in genre_ids:
                                genre = tv_genre_list.get(genre_id=i)
                                genre.contents.add(content)
                                genre.save()
                        elif video["media_type"] == "movie":
                            for i in genre_ids:
                                genre = movie_genre_list.get(genre_id=i)
                                genre.contents.add(content)
                                genre.save()

        self.stdout.write(self.style.SUCCESS(f"Created {count} Trending Contents!"))
