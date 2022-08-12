from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.contrib import messages

from movie.models import Movie, Review
from movie.forms import CreateNewMovieForm, CreateNewReviewForm


@login_required
def index(request):
  return redirect("movie:dashboard")

@login_required
def dashboard(request):
  movies = Movie.objects.all().order_by('-created_ts')
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
    reviews = Review.objects.filter(movie=movie.id)
    return render(request, "movie/movie-page.html", { 'movie': movie, 'reviews': reviews })
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

# REVIEW

@login_required
def createReview(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  if request.method == 'POST':
    form = CreateNewReviewForm(request.POST)
    if form.is_valid():
      form.save(created_by=request.user, movie=movie)
      movie.is_reviewed = True
      movie.save()
      messages.success(request, "Review saved successfully!")
      return redirect('movie:dashboard')
    else:
      messages.error(request, "Errors in form!")
      return render(request, "movie/newReview.html", { 'errors': form.errors })
  else:
    form = CreateNewReviewForm()
  return render(request, 'movie/newReview.html', { 'form': form, 'movie': movie })

@login_required
def deleteReview(request, review_id):
  try:
    review = get_object_or_404(Review, pk=review_id)
    reviews = Review.objects.filter(movie=review.movie)

    # make sure that there are no other reviews for this movie
    # only then, set movie.is_reviewed to False
    if len(reviews) == 1:
      movie = get_object_or_404(Movie, pk=review.movie.id)
      movie.is_reviewed = False
      movie.save()
    review.delete()
    messages.success(request, 'Deleted {}'.format(review_id))
    return redirect('movie:dashboard')
  except Http404:
    messages.error(request, "Couldn't find review with id {}".format(review_id))
    return redirect('movie:dashboard')

@login_required
def updateReview(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  form = CreateNewReviewForm(request.POST or None, instance=review)
  if form.is_valid():
    form.save(created_by=request.user)
    messages.success(request, "Review for {} updated successfully!".format(review.movie))
    return redirect("movie:dashboard")
  return render(request, "movie/updateReview.html", { 'form': form, 'review': review })
