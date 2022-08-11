from django.shortcuts import render, redirect
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
  paginator = Paginator(movies, 2)

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
def updateMovie(request):
  return HttpResponse("UPDATE MOVIE")

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
