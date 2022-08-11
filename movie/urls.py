from django.urls import path

from . import views

app_name = 'movie'

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('', views.index, name='index'),
  path('<str:username>/watchlog/', views.watchlog, name='watchlog'),
  path('<str:username>/watchlist/', views.watchlist, name='watchlist'),
  path('movie/<int:movie_id>/', views.getMovie, name='moviePage'),
  path('new/', views.newMovie, name='new'),
  path('update/<int:movie_id>/', views.updateMovie, name='update'),
  path('delete/<int:movie_id>/', views.deleteMovie, name='delete')
]