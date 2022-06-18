from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("<int:pk>/favs", views.FavsView.as_view(), name="favs"),
    path("<int:pk>/reviews", views.ReviewsView.as_view(), name="reviews"),
    path("<int:pk>/followers", views.FollowersView.as_view(), name="followers"),
    path("<int:pk>/following", views.FollowingView.as_view(), name="following"),
]
