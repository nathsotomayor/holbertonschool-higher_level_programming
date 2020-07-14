-- Lists all cities with id, city and state name
SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s ON c.state_id = s.id ORDER BY c.id ASC;
