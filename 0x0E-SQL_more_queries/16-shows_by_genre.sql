-- Lists all shows and genres
SELECT tv_s.title, tv_g.name FROM tv_shows tv_s
LEFT JOIN tv_show_genres tv_sg ON tv_s.id = tv_sg.show_id
LEFT JOIN tv_genres tv_g ON tv_g.id = tv_sg.genre_id
ORDER BY tv_s.title ASC, tv_g.name;
