WITH turn   AS      (SELECT turn, person_id, person_name, weight, 
                            SUM(weight) OVER(ORDER BY turn ASC) as total_weight
                    FROM    Queue
                    )
SELECT  TOP 1 person_name
FROM    turn
WHERE   total_weight <= 1000
ORDER BY    total_weight DESC