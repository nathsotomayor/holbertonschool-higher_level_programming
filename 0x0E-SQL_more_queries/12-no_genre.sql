-- Lists all shows without a genre
SELECT tv_s.title, tv_sg.genre_id FROM tv_shows tv_s LEFT JOIN tv_show_genres tv_sg ON tv_s.id = tv_sg.show_id WHERE tv_sg.show_id IS NULL ORDER BY tv_s.title ASC, tv_sg.genre_id ASC;
