from django.shortcuts import render
from django.views.generic import ListView, View
from . import models as content_models


class ContentsView(ListView):

    model = content_models.Content
    paginate_by = 10
    context_object_name = "contents"
    template_name = "contents.html"
    


class SingleContentView(View):

    pass


class CreateReviewView(View):

    pass
