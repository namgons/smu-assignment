from django.urls import path
from . import views

app_name = "contents"

urlpatterns = [
    path("<int:pk>/", views.ContentView.as_view(), name="content"),
    path(
        "<int:pk>/reviews/create/",
        views.CreateReviewView.as_view(),
        name="create_reviews",
    ),
]
