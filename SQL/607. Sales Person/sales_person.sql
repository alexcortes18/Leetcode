-- Write your PostgreSQL query statement below

SELECT name
FROM Salesperson sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
    -- AND o.sales_id IS NOT NULL
);