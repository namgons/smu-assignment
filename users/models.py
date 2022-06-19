from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def count_reviews(self):
        return self.reviews.count()

    def __str__(self):
        return self.username
