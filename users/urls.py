from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
    # path("<int:pk>/favs", views.FavsView.as_view(), name="favs"),
]
