from django.shortcuts import render
from django.views.generic import View, DetailView
from . import models as user_models


class LoginView(View):
    pass


class LogoutView(View):
    pass


class ProfileView(DetailView):

    model = user_models.User
    context_object_name = "user"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ob = context["object"]
        context["reviews"] = ob.reviews.all().order_by("-created")
        return context


class FavsView(View):
    pass


class ReviewsView(View):
    pass


class FollowersView(View):
    pass


class FollowingView(View):
    pass
