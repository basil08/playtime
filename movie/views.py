from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.contrib import messages

from movie.models import Movie
from movie.forms import CreateNewMovieForm


@login_required
def index(request):
  return redirect("movie:dashboard")

@login_required
def dashboard(request):
  movies = Movie.objects.all()
  paginator = Paginator(movies, 8)

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'movie/dashboard.html', {'page_obj': page_obj})

def watchlog(request, username):
  print("DEBUG: ", username)
  return HttpResponse("WATCHLOG")

def watchlist(request, username):
  print("DEBUG: ", username)
  return HttpResponse("WATCHLIST")

@login_required
def getMovie(request, movie_id):
  try:
    movie = Movie.objects.get(pk=movie_id)
    return render(request, "movie/movie-page.html", { 'movie': movie })
  except Http404:
    messages.error(request, "Couldn't find movie with id {}".format(movie_id))
    return render(request, "movie/movie-page.html")

@login_required
def newMovie(request):
  if request.method == 'POST':
    form = CreateNewMovieForm(request.POST, request.FILES)
    if form.is_valid():
      form.save(created_by=request.user)
      messages.success(request, "Movie saved successfully!")
      return render(request, "movie/new.html")
    else:
      messages.error(request, "Errors in form!")
      return render(request, "movie/new.html", { 'errors': form.errors })
  else:
    form = CreateNewMovieForm()

  return render(request, 'movie/new.html', { 'form': form })

@login_required
def updateMovie(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  form = CreateNewMovieForm(request.POST or None, request.FILES or None, instance=movie)
  if form.is_valid():
    form.save(created_by=request.user)
    messages.success(request, "{} updated successfully!".format(movie.title))
    return redirect("movie:dashboard")
  return render(request, "movie/update.html", { 'form': form, 'movie_id': movie_id, 'title': movie.title })

  # if request.method == 'POST':
  #   form = CreateNewMovieForm(request.POST, request.FILES)
  #   if form.is_valid():
  #     form.save(created_by=request.user)
  #   else:
  #     messages.error(request, "Errors in form!")
  #     return render(request, "movie/update.html", { 'errors': form.errors })
  # else:
  #   movie = Movie.objects.get(pk=movie_id)
  #   form = CreateNewMovieForm(
  #     initial={
  #       'title': movie.title,
  #       'language': movie.language,
  #       'synopsis': movie.synopsis,
  #       'release_year': movie.release_year,
  #       'directors': movie.directors,
  #       'runtime': movie.runtime,
  #       'genres': movie.genres,
  #       'tags': movie.tags,
  #       'imdb_rating': movie.imdb_rating,
  #       'n_watches': movie.n_watches,
  #       'first_watch': movie.first_watch,
  #       'have_watched': movie.have_watched,
  #       'on_watchlist': movie.on_watchlist
  #     })

  # return render(request, 'movie/update.html', { 'form': form, 'movie_id': movie_id, 'title': movie.title })


@login_required
def deleteMovie(request, movie_id):
  try:
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    messages.success(request, 'Deleted {}'.format(movie.title))
    return redirect('movie:dashboard')
  except Http404:
    messages.error(request, "Couldn't find movie with id {}".format(movie_id))
    return redirect('movie:dashboard')
