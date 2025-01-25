
-- Also Done by ChatGPT. I learned about RANK() and DENSE_RANK()

/* Write your T-SQL query statement below */

SELECT score,
DENSE_RANK() OVER (ORDER BY score DESC) as rank
FROM Scores
ORDER BY score DESC