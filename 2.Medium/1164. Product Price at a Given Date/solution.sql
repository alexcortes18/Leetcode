/* Write your T-SQL query statement below */

-- VERSION 1: 887ms Beats 57.33%
WITH updated_products AS (
    SELECT  product_id, MAX(change_date) AS last_date
    FROM    Products
    WHERE   change_date <= '2019-08-16'
    GROUP BY product_id
)

SELECT  p.product_id,
        COALESCE(p2.new_price,10) AS price
FROM    (
    SELECT DISTINCT product_id FROM Products
) p
LEFT JOIN Products p2
ON      p.product_id = p2.product_id
AND     p2.change_date = (  SELECT last_date
                            FROM    updated_products u
                            WHERE   u.product_id = p.product_id);

-- Second Version:  918ms Beats 46.57%
-- SELECT  product_id,
--         COALESCE(
--             (   SELECT  TOP 1 new_price
--                 FROM    products p2
--                 WHERE   p2.product_id = p1.product_id
--                 AND     change_date <= '2019-08-16'
--                 ORDER BY change_date DESC
--             )
--             ,10) AS price
-- FROM    (SELECT DISTINCT(product_id) FROM products) AS p1;