from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class User(AbstractUser):

    pass


class UserFollowing(core_models.TimeStampedModel):
    user_id = models.ForeignKey(User, related_name="follwing")

    following_user_id = models.ForeignKey(User, related_name="follower")
