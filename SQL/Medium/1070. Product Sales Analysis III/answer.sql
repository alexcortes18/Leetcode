SELECT s.product_id, s.year as first_year, s.quantity, s.price
FROM Sales s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
    ) as first_year_table 
ON s.year = first_year_table.first_year
AND s.product_id = first_year_table.product_id