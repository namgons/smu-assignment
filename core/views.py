from django.shortcuts import render
from django.views.generic import View, ListView
from users import models as user_models
from reviews import models as review_models


class HomeView(ListView):

    model = review_models.Review
    ordering = ("-created",)
    context_object_name = "reviews"
    template_name = "home.html"
    paginate_by = 20
