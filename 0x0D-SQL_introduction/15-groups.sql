-- Lists records with the same score in second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
