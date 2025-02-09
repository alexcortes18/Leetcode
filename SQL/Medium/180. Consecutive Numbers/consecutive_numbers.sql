/* Write your T-SQL query statement below */

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
    LEAD(num, 1) OVER (ORDER BY id) as next1,
    LEAD(num, 2) OVER (ORDER BY id) as next2
    FROM Logs
) AS temp
WHERE num = next1 and num=next2