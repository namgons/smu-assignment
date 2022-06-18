from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("<int:pk>/create/", views.ReviewCreateView.as_view(), name="create"),
]
