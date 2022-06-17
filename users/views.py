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


class FavsView(View):
    pass


class ReviewsView(View):
    pass


class FollowersView(View):
    pass


class FollowingView(View):
    pass
