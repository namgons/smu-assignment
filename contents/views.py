from django.shortcuts import render
from django.views.generic import ListView, View
from . import models as content_models


class MoviesView(ListView):

    model = content_models.Content
    paginate_by = 40
    context_object_name = "contents"
    template_name = "contents/contents.html"

    def get_queryset(self):
        return (
            super().get_queryset().filter(media_type=content_models.Content.TYPE_MOVIE)
        )


class TvsView(ListView):

    model = content_models.Content
    paginate_by = 40
    context_object_name = "contents"
    template_name = "contents/contents.html"

    def get_queryset(self):
        return super().get_queryset().filter(media_type=content_models.Content.TYPE_TV)


class SingleContentView(View):

    pass


class CreateReviewView(View):

    pass
