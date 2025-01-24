-- This is from ChatGPT. Learned new things about using IF (and being/end). 
-- Also learned about OFFSET 1 ROW FECTH NEXT 1 ROW ONLY.


IF (SELECT COUNT(DISTINCT(salary)) FROM Employee) <= 1
BEGIN
    SELECT NULL AS SecondHighestSalary;
END
ELSE
BEGIN
    SELECT salary AS SecondHighestSalary
    FROM (
        SELECT DISTINCT salary
        FROM Employee
        -- GROUP BY salary
        ORDER BY salary DESC
        OFFSET 1 ROW FETCH NEXT 1 ROW ONLY
    ) AS DistinctSalaries;
END