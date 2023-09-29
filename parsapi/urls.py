from django.urls import path

from . import views

urlpatterns = [
    path("patriotic-music/", views.PatrioticMusicVS.as_view(), name="patriotic-music"),
]


