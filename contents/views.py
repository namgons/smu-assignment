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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Movie"
        return context


class TvsView(ListView):

    model = content_models.Content
    paginate_by = 40
    context_object_name = "contents"
    template_name = "contents/contents.html"

    def get_queryset(self):
        return super().get_queryset().filter(media_type=content_models.Content.TYPE_TV)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "TV"
        return context


class SingleContentView(DetailView):

    model = content_models.Content
    context_object_name = "content"
    template_name = "contents/single_content.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ob = context["object"]
        context["reviews"] = ob.reviews.all().order_by("-created")
        return context


class CreateReviewView(View):

    pass
