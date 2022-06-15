from django.core.management import BaseCommand
from users import models as user_models


class Command(BaseCommand):
    def handle(self, *args, **options):

        

        
        self.stdout.write(self.style.SUCCESS(f"Created {count} Trending Contents!"))
