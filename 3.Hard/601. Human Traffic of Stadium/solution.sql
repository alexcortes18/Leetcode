-- Write your PostgreSQL query statement below

WITH    number_people   AS (SELECT  *,
                                    id - ROW_NUMBER() OVER (ORDER BY id asc) AS group_number
                            FROM    Stadium
                            WHERE   people >= 100)

SELECT  id, visit_date, people
FROM    number_people AS np1
WHERE   EXISTS (
    SELECT  1
    FROM    number_people np2
    WHERE    np1.group_number = np2.group_number
    GROUP BY    np2.group_number
    HAVING  COUNT(*) >= 3
)