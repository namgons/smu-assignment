from django.shortcuts import render
from django.views.generic import CreateView
from . import models
from contents import models as content_models


class ReviewCreateView(CreateView):

    model = models.Review
    fields = ("comment",)
    template_name = "reviews/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["content"] = content_models.Content.objects.get(pk=pk)
        return context
