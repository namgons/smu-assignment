from django.core.management import BaseCommand
from genres import models as genre_models
import tmdbsimple as tmdb


class Command(BaseCommand):
    def handle(self, *args, **options):

        tmdb.API_KEY = "cb6371d33ed68513e62d37f350992128"

        tv_genre_list = tmdb.Genres().tv_list()["genres"]
        movie_genre_list = tmdb.Genres().movie_list()["genres"]

        cnt1, cnt2 = 0, 0

        for g in tv_genre_list:
            cnt1 += 1
            name = g["name"]
            genre_id = g["id"]
            media_type = genre_models.Genre.TYPE_TV
            genre_models.Genre.objects.create(
                name=name, genre_id=genre_id, media_type=media_type
            )

        for g in movie_genre_list:
            cnt2 += 1
            name = g["name"]
            genre_id = g["id"]
            media_type = genre_models.Genre.TYPE_TV
            genre_models.Genre.objects.create(
                name=name, genre_id=genre_id, media_type=media_type
            )

        self.stdout.write(self.style.SUCCESS(f"Created {cnt1} TV genres and {cnt2} Movie genres!"))
