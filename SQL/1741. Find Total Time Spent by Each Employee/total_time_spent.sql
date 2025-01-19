/* Write your T-SQL query statement below */

-- this was not too fast, but just the first solution i quickly came up with.

WITH temporal AS (
    SELECT (out_time - in_time) as total_time,
    emp_id,
    event_day,
    in_time,
    out_time
    FROM Employees
)
SELECT 
    e.event_day AS day,
    e.emp_id,
    sum(t.total_time) as total_time
FROM Employees e
JOIN temporal t
ON e.emp_id = t.emp_id AND e.event_day = t.event_day
AND e.in_time = t.in_time AND e.out_time = t.out_time
GROUP BY e.event_day, e.emp_id