SELECT *
FROM Cinema c
WHERE c.description <> 'boring'
AND c.id % 2 <> 0
ORDER BY rating desc