/* Write your T-SQL query statement below */

WITH first_orders AS (
    SELECT  customer_id, MIN(order_date) as first_order
    FROM    delivery
    GROUP BY    customer_id
),
     dates AS (
    SELECT  d.customer_id, d.customer_pref_delivery_date,
            f.first_order    
    FROM    delivery d INNER JOIN first_orders f ON
            d.customer_id = f.customer_id AND d.order_date = f.first_order
)
SELECT  ROUND(SUM(CASE WHEN first_order = customer_pref_delivery_date 
        THEN 1 ELSE 0 END)* 1.0/COUNT(*) *100,2) AS immediate_percentage
FROM    dates;


