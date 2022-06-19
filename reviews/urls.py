from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("<str:slug>/create/", views.ReviewCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", views.review_delete, name="delete"),
    path("<int:pk>/update/", views.ReviewUpdateView.as_view(), name="update"),
]
