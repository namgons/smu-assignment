from django.urls import path
from . import views

app_name = "contents"

urlpatterns = [
    path("movies/", views.MoviesView.as_view(), name="movies"),
    path("tvs/", views.TvsView.as_view(), name="tvs"),
    path("<int:pk>/", views.SingleContentView.as_view(), name="single_content"),
]
