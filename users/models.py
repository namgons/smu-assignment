from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    followings = models.ManyToManyField("User", related_name="followers", blank=True)

    def count_reviews(self):
        return self.reviews.count()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
