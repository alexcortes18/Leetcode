SELECT p.product_id,
ROUND (
    COALESCE(CAST(SUM(u.units*p.price) as FLOAT)/NULLIF(SUM(u.units),0),0), 2
) as average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
AND u.purchase_date BETWEEN p.start_date and p.end_date
GROUP BY p.product_id