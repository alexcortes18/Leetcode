# Write your MySQL query statement below
-- Select e1.name as Employee
-- from Employee e1
-- inner join Employee e2 on e1.managerId = e2.id
-- where e1.salary > e2.salary

SELECT e1.name AS Employee
FROM Employee e1
WHERE EXISTS (
    SELECT 1
    FROM Employee e2
    WHERE e1.managerId = e2.id
    AND e1.salary > e2.salary
);