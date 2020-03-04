-- Write a script that lists all shows, and all genres linked to that show
-- from the database hbtn_0d_tvshows.
SELECT title, name FROM tv_shows, tv_genres FROM tv_shows.title LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN name ON tv_show_genres.genre_id = tv_genres.id ORDER BY title, name ASC;