
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from parsapi.models import CatalogPatrioticMusic
from parsapi.serializers import MuseumFundRFSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PatrioticMusicVS(generics.ListCreateAPIView):
    queryset = CatalogPatrioticMusic.objects.all()
    serializer_class = MuseumFundRFSerializer
    pagination_class = LargeResultsSetPagination

    # def list(self, request, *args, **kwargs):
    #     patriotic_music = CatalogPatrioticMusic.objects.all()
    #     serializer = MuseumFundRFSerializer(patriotic_music, many=True)
    #     return Response({"patriotic-music": serializer.data})
