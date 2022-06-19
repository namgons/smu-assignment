from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
    # path("<int:pk>/favs", views.FavsView.as_view(), name="favs"),
]
