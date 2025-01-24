/* Write your T-SQL query statement below */

SELECT e1.employee_id, e1.name,
COUNT(*) AS reports_count,
ROUND(AVG(CAST(e2.age AS FLOAT)),0) AS average_age
FROM Employees e1
JOIN Employees e2 on e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
ORDER BY e1.employee_id