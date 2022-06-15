from django.db import models
from core import models as core_models
from users import models as user_models
from movies import models as movie_models


class Review(core_models.TimeStampedModel):

    RATING_ONE = 1
    RATING_TWO = 2
    RATING_THREE = 3
    RATING_FOUR = 4
    RATING_FIVE = 5

    RATING_CHOICE = (
        (RATING_ONE, 1),
        (RATING_TWO, 2),
        (RATING_THREE, 3),
        (RATING_FOUR, 4),
        (RATING_FIVE, 5),
    )

    content = models.TextField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICE)

    user = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, related_name="reviews"
    )
    movie = models.ForeignKey(
        movie_models.Movie, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"{self.user} :: {self.movie}"
