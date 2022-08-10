## DEV SPECS

### TARGET: MVP


0. Authentication
1. CRUD Movie Database
2. Add rating, reviews
3. Search features



### MODELS

1. Movie
  a. title: CharField
  b. language: CharField
  c. region: CharField
  d. synopsis: CharField
  e. release_year: Integer
  f. n_watches: Integer
  g. imdb_rating: Floating
  h. runtime: Floating
  i. is_franchise: Boolean
  j. have_watched: Boolean
  k. on_watchlist: Boolean
  l. release_date: Integer
  m. first_watch: Date
  n. directors: CharField
  o. genres: CharField
  p. tags: CharField

  q. created_ts: DateTime
  r. created_by: ForiegnKey
  s. last_updated: DateTime