from django.core.management import BaseCommand
from users import models as user_models
from django_seed import Seed


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):

        number = options.get("number")

        seeder = Seed.seeder()
        faker = Seed.faker("ko_KR")
        user_models.User.objects.create_user
        seeder.add_entity(
            user_models.User,
            number,
            {
                "username": lambda x: faker.name(),
                "first_name": "",
                "last_name": "",
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
