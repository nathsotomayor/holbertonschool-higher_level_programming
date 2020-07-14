-- Lists all cities with id, city and state name
SELECT tv_s.title, tv_sg.genre_id FROM tv_shows tv_s INNER JOIN tv_show_genres tv_sg ON tv_s.id = tv_sg.show_id ORDER BY tv_s.title ASC, tv_sg.genre_id ASC;
