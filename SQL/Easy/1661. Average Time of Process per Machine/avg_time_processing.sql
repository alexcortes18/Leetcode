/* Write your T-SQL query statement below */

-- my result was pretty good: 286ms Beats 74.35%
-- I needed some help with the SUM(CASE...) part.

WITH temp AS (
    SELECT 
        machine_id, 
        process_id,
        SUM(
            CASE 
                WHEN activity_type = 'start' THEN -timestamp
                WHEN activity_type = 'end' THEN timestamp
                END
        ) as process_time
    FROM Activity
    GROUP BY machine_id, process_id
)
SELECT machine_id,
ROUND(AVG(process_time),3) as processing_time
FROM temp
GROUP BY machine_id

-- CHATgpt. also valid:
-- SELECT 
--     machine_id,
--     ROUND(AVG(end_time - start_time), 3) AS processing_time
-- FROM (
--     SELECT 
--         machine_id,
--         process_id,
--         MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time,
--         MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time
--     FROM Activity
--     GROUP BY machine_id, process_id
-- ) AS ProcessTimes
-- GROUP BY machine_id;
