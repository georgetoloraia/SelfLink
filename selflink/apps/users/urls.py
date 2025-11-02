"""URL routes for the users application."""

from django.urls import path

from .views import MeProfileView, ping


app_name = "users"

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("me/", MeProfileView.as_view(), name="me"),
]

