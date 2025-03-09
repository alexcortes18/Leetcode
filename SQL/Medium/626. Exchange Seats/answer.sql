-- Write your PostgreSQL query statement below

-- SELECT id,
--     CASE
--         WHEN id % 2 = 1 AND LEAD(id) OVER (ORDER BY id) IS NULL THEN student
--         WHEN id % 2 = 1 THEN LEAD(student) OVER (ORDER BY id)
--         WHEN id % 2 = 0 THEN LAG(student) OVER (ORDER BY id)
--         ELSE student
--     END AS student
-- FROM Seat

SELECT id,
    COALESCE(
        CASE
            WHEN id % 2 = 1 THEN LEAD(student) OVER (ORDER BY id)
            WHEN id % 2 = 0 THEN LAG(student) OVER (ORDER BY id)
            ELSE student
        END, student) AS student
FROM Seat