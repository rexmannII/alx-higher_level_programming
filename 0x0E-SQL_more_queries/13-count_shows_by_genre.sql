-- Import the database dump from hbtn_0d_tvshows to MySQL server: download (same as 12-no_genre.sql)
--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT name AS genre, COUNT(*) AS number_of_shows  FROM tv__genres
JOIN  tv-show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
