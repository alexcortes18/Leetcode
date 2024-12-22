SELECT c.name AS Customers
FROM Customers c
WHERE c.id != ALL (
    Select o.customerId
    FROM Orders o
)