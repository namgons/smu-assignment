from django.db import models
from contents import models as content_models


class Genre(models.Model):

    TYPE_TV = "tv"
    TYPE_MOVIE = "movie"

    TYPE_CHOICES = (
        (TYPE_TV, "tv"),
        (TYPE_MOVIE, "movie"),
    )

    name = models.CharField(max_length=20)
    genre_id = models.IntegerField()
    media_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    contents = models.ManyToManyField(content_models.Content, related_name="genres")

    def __str__(self):
        return self.name

    def count_contents(self):
        return self.contents.count()
