SELECT query_name, 
ROUND(AVG(CAST(rating AS FLOAT)/position), 2) as quality,
ROUND(CAST(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100 AS FLOAT)/COUNT(*), 2) as poor_query_percentage
FROM Queries
GROUP BY query_name