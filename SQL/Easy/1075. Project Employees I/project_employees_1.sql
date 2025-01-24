-- For T-SQL:
-- SELECT p.project_id, 
-- CAST(ROUND(AVG(experience_years),2) as DECIMAL(10,2)) as average_years
-- FROM Project p JOIN Employee e ON p.employee_id = e.employee_id
-- GROUP BY p.project_id

-- For PostgreSQL:
SELECT p.project_id, 
ROUND(AVG(experience_years),2) as average_years
FROM Project p JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id