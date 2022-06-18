from django.shortcuts import render
from django.views.generic import CreateView
from . import models


class ReviewCreateView(CreateView):

    model = models.Review
    fields = ("comment",)
