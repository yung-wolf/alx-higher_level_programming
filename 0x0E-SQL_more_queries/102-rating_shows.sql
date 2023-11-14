-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
  JOIN tv_show_ratings
  WHERE tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;