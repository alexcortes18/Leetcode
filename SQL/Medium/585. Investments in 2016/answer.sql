/* Write your T-SQL query statement below */

-- No tuples allowed in SQL Server

SELECT ROUND(sum(tiv_2016),2) as tiv_2016
FROM Insurance i1
WHERE tiv_2015 in (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND NOT EXISTS (
    SELECT 1
    FROM Insurance i2
    WHERE i1.pid <> i2.pid
    AND i1.lat = i2.lat
    AND i1.lon = i2.lon
)

-- Write your PostgreSQL query statement below

-- Tuples allowed here. You can also cast faster with  "::cast_type"

SELECT ROUND(sum(tiv_2016)::numeric,2) as tiv_2016
FROM Insurance
WHERE tiv_2015 in (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) in (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)