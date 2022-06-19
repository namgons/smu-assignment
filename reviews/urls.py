from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("<str:slug>/create/", views.ReviewCreateView.as_view(), name="create"),
    path("<str:slug>/delete/", views.review_delete, name="delete"),
]
