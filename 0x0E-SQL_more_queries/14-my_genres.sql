-- hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Each record should display: tv_genres.name
SELECT tv_genres.name
FROM tv_shows
  INNER JOIN tv_show_genres ON tv_shows.title = 'Dexter' AND tv_shows.id = tv_show_genres.show_id
  INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_genres.name;
