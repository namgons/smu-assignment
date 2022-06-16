import random
from secrets import choice
from django.core.management import BaseCommand
from contents import models as content_models
from users import models as user_models
from reviews import models as review_models
from django_seed import Seed


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many reviews do you want to create?",
        )

    def handle(self, *args, **options):

        number = options.get("number")

        seeder = Seed.seeder()
        faker = Seed.faker("ko_KR")

        all_users = user_models.User.objects.all()
        all_contents = content_models.Content.objects.all()

        seeder.add_entity(
            review_models.Review,
            number,
            {
                "comment": lambda x: faker.paragraph(nb_sentences=random.randint(2, 5)),
                "user": lambda x: random.choice(all_users),
                "content": lambda x: random.choice(all_contents),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
