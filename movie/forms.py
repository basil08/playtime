from django import forms
import time
from movie.models import Movie

def save_image_file(fp, name, width, height, extension='jpeg'):
  if not name: name = int(time.time())
  img_url = "img/posters/IMG{}_{}X{}.{}".format(name, width, height, extension)

  # NOTE: A tiny hack to accomodate the img/ directory inside static/ AND
  # access using {% static %} tag
  # db only stores the part _after_ static (that is, relative to static/)
  # AND NOT the absolute path relative to project root
  with open('./static/' + img_url, 'wb+') as dest:
    for chunk in fp.chunks():
      dest.write(chunk)
  return img_url

class CreateNewMovieForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = (
      'title',
      'language',
      'synopsis',
      'release_year',
      'release_date',
      'directors',
      'runtime',
      'genres',
      'tags',
      'imdb_rating',
      'n_watches',
      'first_watch',
      'have_watched',
      'on_watchlist',
      'music_by',
      'distributor',
      'trailer_url',
      'trailer_video',
      'is_franchise',
      'franchise_movies',
      'based_on'
    )
    labels = {
      'n_watches': 'Number of watches'
    }
  poster_image = forms.ImageField(label='Poster Image', required=False)

  def __init__(self, *args, **kwargs):
    super(CreateNewMovieForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      if field != 'have_watched' and field != 'on_watchlist' and field != 'is_franchise':
        self.fields[field].widget.attrs.update({
          'class': 'form-control',
          'placeholder': None
        })
      else:
        self.fields[field].widget.attrs.update({
          'class': 'form-check-input'
      })


  def save(self, commit=True, *args, **kwargs):
    movie = super(CreateNewMovieForm, self).save(commit=False)
    created_by = kwargs.pop('created_by', None)
    if not created_by:
      raise forms.ValidationError("NO USER ID FOUND")

    img = self.cleaned_data['poster_image']

    if img:
      poster_image_url = save_image_file(img, img.image.filename, img.image.width, img.image.height, img.image.format.lower())
      movie.poster_image = poster_image_url
    movie.created_by = created_by
    if commit:
      movie.save()
    return movie