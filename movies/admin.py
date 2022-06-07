from django.contrib import admin
from . import models as movie_models


@admin.register(movie_models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "get_total_rate",
    )
