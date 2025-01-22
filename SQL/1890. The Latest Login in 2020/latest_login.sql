/* Write your T-SQL query statement below */

SELECT  user_id, 
        max(time_stamp) AS last_stamp
FROM (
    SELECT user_id, time_stamp
    FROM Logins
    WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
) AS logins_temp
GROUP BY user_id

-- ChatGpt more condense.
-- SELECT user_id, 
--        MAX(time_stamp) AS last_stamp
-- FROM Logins
-- WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
-- GROUP BY user_id;