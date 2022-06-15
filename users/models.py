from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class User(AbstractUser):

    pass


class UserFollowing(core_models.TimeStampedModel):
    following_target_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follwing"
    )

    following_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )
