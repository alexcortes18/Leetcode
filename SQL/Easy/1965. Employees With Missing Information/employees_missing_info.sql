/* Write your T-SQL query statement below */

SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Salaries
)
UNION ALL
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Employees
)
ORDER BY employee_id ASC

-- ChatGPT, more efficient:
SELECT COALESCE(e.employee_id, s.employee_id) AS employee_id
-- SELECT e.employee_id, s.employee_id, e.name, s.salary
FROM Employees e
FULL OUTER JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE e.employee_id IS NULL OR s.employee_id IS NULL
ORDER BY employee_id ASC