from django.urls import path
import views

app_name = "users"

urlspatterns = [
    path("login/", views.LoginView().as_view(), name="login"),
    path("logout/", views.LogoutView().as_view(), name="logout"),
    path("<int:id>/", views.ProfileView.as_view(), name="profile"),
    path("<int:id>/favs", views.FavsView.as_view(), name="favs"),
    path("<int:id>/reviews", views.ReviewsView.as_view(), name="reviews"),
    path("<int:id>/followers", views.FollowersView.as_view(), name="followers"),
    path("<int:id>/following", views.FollowingView.as_view(), name="following"),
]
