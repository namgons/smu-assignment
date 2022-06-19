from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class User(AbstractUser):
    def count_following(self):
        return self.following.count()

    def count_followers(self):
        return self.followers.count()

    def count_reviews(self):
        return self.reviews.count()

    def __str__(self):
        return self.username


class UserFollowing(core_models.TimeStampedModel):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )

    following_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )

    def __str__(self):
        return f"{self.user_id} → {self.following_user_id}"
