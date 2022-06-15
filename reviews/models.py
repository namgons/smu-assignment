from django.db import models
from core import models as core_models
from users import models as user_models
from contents import models as content_models


class Review(core_models.TimeStampedModel):

    comment = models.TextField(max_length=200)

    user = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, related_name="reviews"
    )
    content = models.ForeignKey(
        content_models.Content, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"{self.user} :: {self.content}"
