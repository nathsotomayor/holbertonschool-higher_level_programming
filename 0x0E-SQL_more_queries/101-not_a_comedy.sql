-- Lists all shows without genre Comedy 
SELECT DISTINCT tv_s.title FROM tv_shows tv_s
LEFT JOIN tv_show_genres tv_sg ON tv_s.id = tv_sg.show_id
LEFT JOIN tv_genres tv_g ON tv_g.id = tv_sg.genre_id
WHERE tv_s.title NOT IN (
SELECT tv_s.title FROM tv_shows tv_s
INNER JOIN tv_show_genres tv_sg ON tv_s.id = tv_sg.show_id
INNER JOIN tv_genres tv_g ON tv_g.id = tv_sg.genre_id
WHERE tv_g.name = 'Comedy'
)
ORDER BY tv_s.title ASC;
