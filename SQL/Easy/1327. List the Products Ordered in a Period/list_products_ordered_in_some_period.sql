SELECT p.product_name, orders.unit
FROM Products p
JOIN (
    SELECT product_id, SUM(unit) AS unit
    FROM Orders
    WHERE month(order_date) = 2
    AND YEAR(order_date) = 2020
    GROUP BY product_id
) as orders
ON p.product_id = orders.product_id
WHERE orders.unit >= 100