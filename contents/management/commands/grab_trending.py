from django.core.management import BaseCommand
from contents import models as content_models
import tmdbsimple as tmdb


class Command(BaseCommand):
    def handle(self, *args, **options):

        tmdb.API_KEY = "cb6371d33ed68513e62d37f350992128"

        count = 1

        for i in range(1, 5):
            for video in tmdb.Trending().info(page=i)["results"]:
                try:
                    content_models.Content.objects.get(pk=video["id"])
                except content_models.Content.DoesNotExist:
                    count += 1
                    if video["media_type"] == "tv":
                        title = video["name"]
                        released = video["first_air_date"]
                        media_type = content_models.Content.TYPE_TV
                    elif video["media_type"] == "movie":
                        title = video["title"]
                        released = video["release_date"]
                        media_type = content_models.Content.TYPE_MOVIE

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
