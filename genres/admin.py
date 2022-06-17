from django.contrib import admin
from . import models as genre_models


@admin.register(genre_models.Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "count_contents",
        "media_type",
    )
