from django.urls import path
import views

app_name = "movies"

urlspatterns = [
    path("<int:pk>/", views.MovieView.as_view(), name="movie"),
    path(
        "<int:pk>/reviews/create",
        views.CreateReviewView.as_view(),
        name="create_reviews",
    ),
]
