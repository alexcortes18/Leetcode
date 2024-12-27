/* Write your T-SQL query statement below */

SELECT activity_date as day,
COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN CAST(DATEADD(DAY, -29, '2019-07-27') AS DATE) AND '2019-07-27'
-- or also:
-- WHERE activity_date > CAST(DATEADD(DAY, -30, '2019-07-27') AS DATE)
-- AND activity_date <= '2019-07-27'
GROUP BY activity_date
-- HAVING COUNT(*) > 0