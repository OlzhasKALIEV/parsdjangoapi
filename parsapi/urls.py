from django.urls import path

from .views import PatrioticMusicVS, PatrioticMusicRUD, PatrioticMusicDetailView, PatrioticMusicComposerGenre

urlpatterns = [
    path("patriotic-music/", PatrioticMusicVS.as_view(), name="patriotic-music"),
    path("patriotic-music/<int:pk>/", PatrioticMusicRUD.as_view(), name="patriotic-music-pk"),
    path("patriotic-music", PatrioticMusicDetailView.as_view(), name="patriotic-music-id"),
    path("patriotic-music/music", PatrioticMusicComposerGenre.as_view(), name="music"),
]
