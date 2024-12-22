SELECT DISTINCT p1.email as Email
FROM Person p1
GROUP BY p1.email
HAVING COUNT(*) > 1