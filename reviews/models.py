from django.db import models
from core import models as core_models
from users import models as user_models
from movies import models as movie_models


class Review(core_models.TimeStampedModel):

    RATE_ONE = 1
    RATE_TWO = 2
    RATE_THREE = 3
    RATE_FOUR = 4
    RATE_FIVE = 5

    RATE_CHOICE = (
        (RATE_ONE, 1),
        (RATE_TWO, 2),
        (RATE_THREE, 3),
        (RATE_FOUR, 4),
        (RATE_FIVE, 5),
    )

    content = models.TextField(max_length=200)
    rate = models.IntegerField(choices=RATE_CHOICE)

    user = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, related_name="reviews"
    )
    movie = models.ForeignKey(
        movie_models.Movie, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"{self.user} :: {self.movie}"
