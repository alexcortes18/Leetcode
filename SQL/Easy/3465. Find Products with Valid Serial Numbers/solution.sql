-- Write your PostgreSQL query statement below

SELECT product_id, product_name, description
FROM products
WHERE description ~ '(^|[^A-Za-z])SN[0-9]{4}-[0-9]{4}([^0-9]|$)'
ORDER BY product_id;