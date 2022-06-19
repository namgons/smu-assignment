from django.urls import reverse
from django.db import models


class Content(models.Model):

    TYPE_TV = "tv"
    TYPE_MOVIE = "movie"

    TYPE_CHOICES = (
        (TYPE_TV, "tv"),
        (TYPE_MOVIE, "movie"),
    )

    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, null=True)
    overview = models.TextField(max_length=150, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    released = models.DateField(null=True)
    poster_path = models.URLField(null=True)
    media_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title

    def count_reviews(self):
        return self.reviews.count()

    def get_absolute_url(self):
        return reverse("contents:single_content", kwargs={"pk": self.pk})
