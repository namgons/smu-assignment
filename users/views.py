from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, DetailView, FormView
from . import models, forms, mixins


class SignupView(mixins.LoggedOutOnlyView, FormView):

    template_name = "users/signup.html"
    success_url = reverse_lazy("core:home")
    form_class = forms.SignupForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["password1"].label = "Password Confirmation"
        return form


class LoginView(mixins.LoggedOutOnlyView, View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", context={"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


class ProfileView(DetailView):

    model = models.User
    context_object_name = "user_obj"
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
