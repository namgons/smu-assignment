from django.core.management import BaseCommand
from movies import models as movie_models
import tmdbsimple as tmdb


class Command(BaseCommand):
    def handle(self, *args, **options):

        tmdb.API_KEY = "cb6371d33ed68513e62d37f350992128"

        for i in range(1, 10):
            for video in tmdb.Trending().info(page=i)["results"]:
                try:
                    movie_models.Movie.objects.get(pk=video["id"])
                except:
                    if video["media_type"] == "tv":
                        title = video["name"]
                        released = video["first_air_date"]
                        media_type = movie_models.Movie.TYPE_TV
                    if video["media_type"] == "movie":
                        title = video["title"]
                        released = video["release_date"]
                        media_type = movie_models.Movie.TYPE_MOVIE

                    pk = video["id"]
                    overview = video["overview"]
                    rating = video["vote_average"]
                    poster_path = video["poster_path"]

                    movie_models.Movie.objects.create(
                        title=title,
                        pk=pk,
                        overview=overview,
                        rating=rating,
                        released=released,
                        poster_path=f"https://www.themoviedb.org/t/p/w1280/{poster_path}",
                        media_type=media_type,
                    )

        self.stdout.write(self.style.SUCCESS("Connection Succeed!"))
