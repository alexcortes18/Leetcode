SELECT current_.id as Id
FROM Weather as current_ JOIN Weather as previous
ON previous.recordDate = DATEADD(day, -1, current_.recordDate)
WHERE current_.temperature > previous.temperature