from django.urls import path
import views

app_name = "core"


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
