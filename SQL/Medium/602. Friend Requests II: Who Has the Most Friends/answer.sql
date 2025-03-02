-- Write your PostgreSQL query statement below

SELECT id, sum(counts) as num
FROM (
    SELECT requester_id AS id, COUNT(*) AS counts
    FROM RequestAccepted
    GROUP BY requester_id
    UNION ALL
    SELECT accepter_id AS id, COUNT(*) AS counts
    FROM RequestAccepted
    GROUP BY accepter_id
)
GROUP BY id
ORDER BY num DESC
LIMIT 1