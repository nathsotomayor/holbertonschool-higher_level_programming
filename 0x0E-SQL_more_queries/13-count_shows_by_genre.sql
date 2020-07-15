-- Lists all genres and number of shows linked to each
SELECT tv_g.name AS genre, COUNT(tv_sg.genre_id) AS number_of_shows FROM tv_genres tv_g LEFT JOIN tv_show_genres tv_sg ON tv_g.id = tv_sg.genre_id GROUP BY genre ORDER BY number_of_shows DESC;
