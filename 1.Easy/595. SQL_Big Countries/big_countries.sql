# Write your MySQL query statement below

-- Select name, population, area
-- From World
-- where population >= 25000000 or area >= 3000000


Select name, population, area
from World
where area >= 3000000

UNION

Select name, population, area
from World
where population >= 25000000
