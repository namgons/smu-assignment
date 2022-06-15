from django.urls import path
from . import views

app_name = "contents"

urlpatterns = [
    path("", views.ContentsView.as_view(), name="contents"),
    path("<int:pk>/", views.SingleContentView.as_view(), name="single_content"),
    path(
        "<int:pk>/reviews/create/",
        views.CreateReviewView.as_view(),
        name="create_reviews",
    ),
]
