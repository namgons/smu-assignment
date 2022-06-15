from django.contrib import admin
from contents import models as content_models


@admin.register(content_models.Content)
class ContentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "rating",
        "released",
        "media_type",
    )

    list_filter = ("media_type",)

    ordering = (
        "title",
        "released",
    )
