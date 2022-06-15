from django.core.management import BaseCommand
from tmdb3 import set_key


class Command(BaseCommand):
    def handle(self, *args, **options):

        set_key("cb6371d33ed68513e62d37f350992128")

        self.stdout.write(self.style.SUCCESS("Connection Succeed!"))
