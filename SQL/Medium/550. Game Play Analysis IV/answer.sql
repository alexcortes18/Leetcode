/* Write your T-SQL query statement below */

WITH FirstLogin AS (
    SELECT player_id, 
           MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
),
ConsecutiveAfterFirstLogin AS (
    SELECT f.player_id
    FROM FirstLogin f
    JOIN Activity a
      ON f.player_id = a.player_id 
     AND f.first_date = DATEADD(day, -1, a.event_date)
)

SELECT 
    ROUND(CAST(COUNT(DISTINCT player_id) AS FLOAT) 
          / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM ConsecutiveAfterFirstLogin;



-- Basically done by ChatGPT but i understood the logic.