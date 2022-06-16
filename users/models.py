from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class User(AbstractUser):
    def count_following(self):
        return self.follower.count()

    def count_followers(self):
        return self.following.count()


class UserFollowing(core_models.TimeStampedModel):
    following_target_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )

    following_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )

    def __str__(self):
        return f"{self.following_user} → {self.following_target_user}"
