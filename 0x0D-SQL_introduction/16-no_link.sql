-- Lists all score and name records in second_table
-- Order by score and descending with name not null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
