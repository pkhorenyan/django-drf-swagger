from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(
        queryset=Artist.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Album
        fields = ["id", "title", "year", "artist"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title"]


class AlbumSongSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(
        queryset=Album.objects.all(),
        slug_field="title"
    )
    song = serializers.SlugRelatedField(
        queryset=Song.objects.all(),
        slug_field="title"
    )

    class Meta:
        model = AlbumSong
        fields = ["id", "album", "song", "track_number"]
