/* Write your T-SQL query statement below */

WITH polarized_opinions AS (
    SELECT  book_id, COUNT(session_id) AS num_sessions,
            MAX(session_rating) - MIN(session_rating) AS rating_spread,
            (SUM(CASE WHEN session_rating <= 2 THEN 1 ELSE 0 END) +
            SUM(CASE WHEN session_rating >= 4 THEN 1 ELSE 0 END)) * 1.0
            /COUNT(*) AS polarization_score
    FROM    reading_sessions r1
    GROUP BY  book_id
    HAVING   SUM(CASE WHEN session_rating <=2 THEN 1 ELSE 0 END) > 0
    AND      SUM(CASE WHEN session_rating >=4 THEN 1 ELSE 0 END) > 0
    AND      COUNT(session_id) >= 5 
)
SELECT  b.book_id, b.title, b.author, b.genre, b.pages,
        rating_spread,
        ROUND(po.polarization_score,2) AS polarization_score
FROM    books b INNER JOIN polarized_opinions po ON b.book_id = po.book_id
WHERE   po.polarization_score >= 0.6
ORDER BY    po.polarization_score DESC, b.title DESC;