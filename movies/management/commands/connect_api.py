from django.core.management import BaseCommand
from tmdb3 import set_key, tmdb_api, Movie


class Command(BaseCommand):
    def handle(self, *args, **options):

        print(dir(tmdb_api))

        # set_key("cb6371d33ed68513e62d37f350992128")

        # print(Movie.toprated())

        self.stdout.write(self.style.SUCCESS("Connection Succeed!"))
