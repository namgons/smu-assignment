from django.core.management import BaseCommand
import tmdbsimple as tmdb


class Command(BaseCommand):
    def handle(self, *args, **options):

        tmdb.API_KEY = "cb6371d33ed68513e62d37f350992128"

        for i in range(1, 20):
            for m in tmdb.Trending().info(page=i)["results"]:
                title = ""
                try:
                    title = m["title"]
                except:
                    title = m["name"]
                print(title)

        self.stdout.write(self.style.SUCCESS("Connection Succeed!"))
