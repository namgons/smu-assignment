from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("<int:pk>/followers", views.FollowersView.as_view(), name="followers"),
    path("<int:pk>/followings", views.FollowingsView.as_view(), name="followings"),
    path("<int:pk>/follow", views.follow, name="follow"),
    path("<int:pk>/unfollow", views.unfollow, name="unfollow"),
    # path("<int:pk>/favs", views.FavsView.as_view(), name="favs"),
]
