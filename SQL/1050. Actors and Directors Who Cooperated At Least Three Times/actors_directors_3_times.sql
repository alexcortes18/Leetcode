/* Write your T-SQL query statement below */

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3

-- This is 92% faster than the rest! Unexpected and at first try too :)