from django.shortcuts import render

from rest_framework import viewsets
from .models import Artist, Album, Song, AlbumSong
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, AlbumSongSerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Music Catalog API</h1><p>Перейдите на <a href='/swagger/'>Swagger</a> для тестирования API</p>")


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumSongViewSet(viewsets.ModelViewSet):
    queryset = AlbumSong.objects.all()
    serializer_class = AlbumSongSerializer

