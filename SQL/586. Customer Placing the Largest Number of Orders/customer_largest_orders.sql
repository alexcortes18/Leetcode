-- POSTGRESQL:
-- If SQL language or platform has "LIMIT" keyword
-- SELECT customer_number
-- FROM Orders
-- GROUP BY customer_number
-- ORDER BY COUNT(*) DESC
-- LIMIT 1

-- If no "LIMIT" keyword:
Select customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(*) = (
    SELECT MAX(order_count)
    FROM (
        SELECT COUNT(*) as order_count
        FROM Orders
        GROUP BY customer_number
    )
)
