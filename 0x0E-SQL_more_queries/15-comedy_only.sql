-- Lists all Comedy shows 
SELECT tv_s.title FROM tv_shows tv_s
INNER JOIN tv_show_genres tv_sg ON tv_s.id = tv_sg.show_id
INNER JOIN tv_genres tv_g ON tv_g.id = tv_sg.genre_id
WHERE tv_g.name = 'Comedy'
ORDER BY tv_s.title ASC;
