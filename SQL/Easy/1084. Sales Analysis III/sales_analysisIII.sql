-- PostgreSQL:

SELECT DISTINCT p.product_id, p.product_name
FROM PRODUCT p JOIN SALES s ON p.product_id = s.product_id
WHERE s.sale_date >= '2019/01/01' and s.sale_date <='2019/03/31'
and p.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date < '2019/01/01' or sale_date >'2019/03/31'
)