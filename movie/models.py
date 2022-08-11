from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
  title = models.CharField(max_length=300)
  language = models.CharField(max_length=100, null=True, blank=True)
  synopsis = models.TextField(max_length=500, null=True, blank=True)
  release_year = models.IntegerField(null=True, blank=True)
  directors = models.CharField(max_length=400, null=True, blank=True)
  genres = models.CharField(max_length=400, null=True, blank=True)
  tags = models.CharField(max_length=400, null=True, blank=True)
  imdb_rating = models.FloatField(null=True, blank=True)
  runtime = models.FloatField(null=True, blank=True)
  poster_image = models.CharField(max_length=300, null=True, blank=True)

  n_watches = models.IntegerField(null=True, blank=True)
  have_watched = models.BooleanField(default=False)
  on_watchlist = models.BooleanField(default=False)
  first_watch = models.DateField(null=True, blank=True)

  created_ts = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  last_updated = models.DateTimeField(auto_now=True)