/* Write your T-SQL query statement below */

WITH temporal AS (
    SELECT
        COUNT(*) AS number_departments,
        employee_id
    FROM Employee
    GROUP BY employee_id
)
SELECT  e.employee_id, e.department_id
FROM Employee e
JOIN temporal t ON e.employee_id = t.employee_id
WHERE e.primary_flag = 'Y'
OR t.number_departments = 1

-- ChatGPT... makes sense.
-- SELECT employee_id, department_id
-- FROM Employee
-- WHERE primary_flag = 'Y'
-- UNION ALL
-- SELECT employee_id, department_id
-- FROM Employee
-- WHERE primary_flag = 'N'
--   AND employee_id NOT IN (
--       SELECT employee_id
--       FROM Employee
--       WHERE primary_flag = 'Y'
--   );