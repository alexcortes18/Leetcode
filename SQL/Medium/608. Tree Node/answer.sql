-- Write your PostgreSQL query statement below

SELECT t.id,
    CASE
        WHEN t.p_id is NULL THEN 'Root'
        WHEN t.id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS type --needed to name the column
FROM Tree t