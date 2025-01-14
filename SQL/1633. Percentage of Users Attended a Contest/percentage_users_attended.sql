/* Write your T-SQL query statement below */


-- THIS Query is HIGHLY innefficient... took too much time trying to make it work faster but couldn't. so next exercise...

DECLARE @total_users INT;
SELECT @total_users = COUNT(DISTINCT user_id)
FROM Users;

SELECT r.contest_id,
ROUND(
    (COUNT(*) * 100.0) / --before i did CAST(COUNT(*) AS FLOAT) ; maybe CAST is too slow
    -- NULLIF((SELECT COUNT(DISTINCT(user_id)) FROM Users),0) 
    -- NULLIF(@total_users,0)
    @total_users
    , 2) as percentage
FROM Users u JOIN Register R ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC