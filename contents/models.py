from django.db import models


class Movie(models.Model):

    TYPE_TV = "tv"
    TYPE_MOVIE = "movie"

    TYPE_CHOICES = (
        (TYPE_TV, "tv"),
        (TYPE_MOVIE, "movie"),
    )

    title = models.CharField(max_length=30)
    overview = models.TextField(max_length=150, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    released = models.DateField()
    poster_path = models.URLField(null=True)
    media_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title
