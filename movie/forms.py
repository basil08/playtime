from django import forms

from movie.models import Movie

class CreateNewMovieForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = (
      'title',
      'language',
      'synopsis',
      'release_year',
      'directors',
      'genres',
      'tags',
      'imdb_rating',
      'n_watches',
      'first_watch',
      'have_watched',
      'on_watchlist',
    )
    labels = {
      'n_watches': 'Number of watches'
    }

  def __init__(self, *args, **kwargs):
    super(CreateNewMovieForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      if field != 'have_watched' and field != 'on_watchlist':
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
    movie.created_by = created_by
    if commit:
      movie.save()
    return movie