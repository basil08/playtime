from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Movie(models.Model):
  title = models.CharField(max_length=300)
  language = models.CharField(max_length=100, null=True, blank=True)
  music_by = models.CharField(max_length=200, null=True, blank=True)
  distributor = models.CharField(max_length=200, null=True, blank=True)

  synopsis = models.TextField(max_length=500, null=True, blank=True)
  release_year = models.IntegerField(null=True, blank=True)
  release_date = models.DateField(null=True, blank=True)
  directors = models.CharField(max_length=400, null=True, blank=True)

  trailer_video = EmbedVideoField(null=True, blank=True)
  is_franchise = models.BooleanField(default=False)
  franchise_movies = models.CharField(max_length=500, null=True, blank=True)

  based_on = models.CharField(max_length=200, null=True, blank=True)

  genres = models.CharField(max_length=400, null=True, blank=True)
  tags = models.CharField(max_length=400, null=True, blank=True)
  imdb_rating = models.FloatField(null=True, blank=True)
  runtime = models.FloatField(null=True, blank=True)
  poster_image = models.CharField(max_length=300, null=True, blank=True)

  n_watches = models.IntegerField(null=True, blank=True)
  have_watched = models.BooleanField(default=False)
  on_watchlist = models.BooleanField(default=False)
  first_watch = models.DateField(null=True, blank=True)
  is_reviewed = models.BooleanField(default=False)

  created_ts = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  last_updated = models.DateTimeField(auto_now=True)

class Review(models.Model):
  title = models.CharField(max_length=100, null=True, blank=True)
  text = models.TextField()
  rating = models.FloatField(default=1.0)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  created_ts = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  last_updated = models.DateTimeField(auto_now=True)
