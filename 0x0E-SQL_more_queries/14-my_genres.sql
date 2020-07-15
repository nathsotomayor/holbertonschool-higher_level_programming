-- Lists all genres of the show Dexter
SELECT tv_g.name FROM tv_genres tv_g
INNER JOIN tv_show_genres tv_sg ON tv_g.id = tv_sg.genre_id
INNER JOIN tv_shows tv_s ON tv_s.id = tv_sg.show_id
WHERE tv_s.title = 'Dexter'
ORDER BY tv_g.name ASC;
