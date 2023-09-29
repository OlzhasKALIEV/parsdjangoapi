from django.http import JsonResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

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


class PatrioticMusicRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatalogPatrioticMusic.objects.all()
    serializer_class = MuseumFundRFSerializer


class PatrioticMusicDetailView(APIView):

    def get(self, request):
        id = request.GET.get('id')
        try:
            music = CatalogPatrioticMusic.objects.get(pk=id)
            data = {
                'id': music.id,
                'fullname': music.fullname,
                'composer': music.composer,
                'genre': music.genre,
                'theme': music.theme,
                'creationyear': music.creationyear,
            }
            return Response({"results": data})
        except CatalogPatrioticMusic.DoesNotExist:
            return JsonResponse({'error': 'Music not found'}, status=404)

    def put(self, request):
        id = request.GET.get('id')
        try:
            music = CatalogPatrioticMusic.objects.get(pk=id)
            # Обновление полей модели
            music.composer = request.data.get('composer')
            music.fullname = request.data.get('fullname')
            music.save()
            return Response({'success': 'Music updated'})
        except CatalogPatrioticMusic.DoesNotExist:
            return Response({'error': 'Music not found'}, status=404)

    def delete(self, request):
        id = request.GET.get('id')
        try:
            music = CatalogPatrioticMusic.objects.get(pk=id)
            music.delete()
            return Response({'success': 'Music deleted'})
        except CatalogPatrioticMusic.DoesNotExist:
            return Response({'error': 'Music not found'}, status=404)


class PatrioticMusicComposerGenre(APIView):
    serializer_class = MuseumFundRFSerializer

    def get(self, request):
        composer = request.GET.get('composer')
        genre = request.GET.get('genre')

        try:
            if composer:
                music = CatalogPatrioticMusic.objects.filter(composer=composer)
            elif genre:
                music = CatalogPatrioticMusic.objects.filter(genre=genre)
            else:
                return Response({'error': 'No search parameters provided'}, status=400)

            if len(music) == 0:
                return Response({"results": "Music not found"})

            serializers = MuseumFundRFSerializer(music, many=True)
            return Response({"results": serializers.data})
        except CatalogPatrioticMusic.DoesNotExist:
            return Response({'error': 'Music not found'}, status=404)