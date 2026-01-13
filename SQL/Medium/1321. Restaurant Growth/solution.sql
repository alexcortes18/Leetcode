/* Write your T-SQL query statement below */

WITH daily_avg AS (
    SELECT  visited_on,   
            SUM(amount) AS total_amount
    FROM    Customer
    GROUP BY    visited_on
)
SELECT  visited_on, amount, average_amount
FROM (
    SELECT  visited_on,
        SUM(total_amount) OVER(
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(total_amount*1.0) OVER(
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
FROM    daily_avg
)as temp
WHERE   visited_on >= DATEADD(DAY, 6,(SELECT MIN(visited_on) FROM CUSTOMER))
ORDER BY    visited_on