from django.core.management import BaseCommand
from contents import models as content_models
from genres import models as genre_models
import tmdbsimple as tmdb


class Command(BaseCommand):
    def handle(self, *args, **options):

        tmdb.API_KEY = "cb6371d33ed68513e62d37f350992128"

        count = 0

        tv_genre_list = tmdb.Genres().tv_list()["genres"]
        movie_genre_list = tmdb.Genres().movie_list()["genres"]

        print(tv_genre_list)
        print(movie_genre_list)

        for i in range(1, 5):
            for video in tmdb.Trending().info(page=i)["results"]:
                try:
                    content_models.Content.objects.get(pk=video["id"])
                except content_models.Content.DoesNotExist:
                    count += 1

                    genre_ids = video["genre_ids"]

                    for i in genre_ids:
                        if i not in movie_genre_list:
                            print("@@@@@")

                    if video["media_type"] == "tv":
                        title = video["name"]
                        released = video["first_air_date"]
                        media_type = content_models.Content.TYPE_TV

                        for i in genre_ids:
                            if i not in tv_genre_list:
                                print("@@@@@")

                    elif video["media_type"] == "movie":
                        title = video["title"]
                        released = video["release_date"]
                        media_type = content_models.Content.TYPE_MOVIE

                        for i in genre_ids:
                            if i not in movie_genre_list:
                                print("@@@@@")

                    pk = video["id"]
                    overview = video["overview"]
                    rating = video["vote_average"]
                    poster_path = video["poster_path"]

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

        self.stdout.write(self.style.SUCCESS(f"Created {count} Trending Contents!"))
