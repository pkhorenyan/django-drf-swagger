from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.year})"


class Song(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, related_name="album_songs", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="song_albums", on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ("album", "track_number")
        ordering = ["track_number"]

    def __str__(self):
        return f"{self.track_number}. {self.song.title} ({self.album.title})"

