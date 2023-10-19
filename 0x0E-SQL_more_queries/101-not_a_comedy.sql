-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows
WHERE title NOT IN (
SELECT tv_shows.title
FROM tv_shows
  INNER JOIN tv_show_genres
WHERE tv_show_genres.genre_id = 5 AND tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title
) ORDER BY title;
