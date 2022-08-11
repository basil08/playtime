## DEV SPECS

### TODO

~1. Icons~
~2. Sidebar~
3. moviePage
4. Dynamic quote; login page
5. Use S3 for storing posters
6.


### TARGET: MVP


~0. Authentication~
~1. CRUD Movie Database~
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

  t. poster_image: CharField