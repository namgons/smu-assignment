from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
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


class SingleContentView(DetailView):

    model = content_models.Content
    context_object_name = "content"
    template_name = "contents/single.html"


class CreateReviewView(View):

    pass
