from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("<int:pk>/", views.MovieView.as_view(), name="movie"),
    path(
        "<int:pk>/reviews/create/",
        views.CreateReviewView.as_view(),
        name="create_reviews",
    ),
]
