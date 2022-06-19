import random
from django.core.management import BaseCommand
from users import models as user_models
from django_seed import Seed


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many relationships do you want to create?",
        )

    def handle(self, *args, **options):

        number = options.get("number")

        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()

        for _ in range(number):
            user_id, following_user_id = random.choices(all_users, k=2)

            user_models.UserFollowing.objects.create(
                user_id=user_id,
                following_user_id=following_user_id,
            )

        # seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} relationships created!"))
