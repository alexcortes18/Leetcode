SELECT MAX(nums) as num
FROM (
    SELECT num as nums
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) <= 1
) as max_num
