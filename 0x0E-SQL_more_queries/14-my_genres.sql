-- hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Each record should display: tv_genres.name
SELECT tv_genres.name
FROM tv_genres
  INNER JOIN tv_show_genres
WHERE tv_show_genres.show_id = 8 AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_genres.name;
