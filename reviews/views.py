from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from . import models
from contents import models as content_models
from users import mixins as user_mixins


class ReviewCreateView(user_mixins.LoggedInOnlyView, CreateView):

    model = models.Review
    fields = ("comment",)
    template_name = "reviews/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        context["content"] = content_models.Content.objects.get(slug=slug)
        return context

    def form_valid(self, form):
        comment = form.cleaned_data["comment"]
        user = self.request.user
        slug = self.kwargs["slug"]
        content = content_models.Content.objects.get(slug=slug)
        models.Review.objects.create(comment=comment, user=user, content=content)
        return redirect(reverse("contents:single_content", kwargs={"slug": slug}))


def review_delete(request, slug):
    review = models.Review.objects.get(slug=slug)

    if request.method == "POST":
        review.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
