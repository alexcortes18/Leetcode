/* Write your T-SQL query statement below */

WITH rc AS (
    SELECT      user_id,
                rated_movies,
                RANK() OVER(ORDER BY rated_movies DESC) AS rankings
    FROM
        (
            SELECT      user_id, COUNT(*) AS rated_movies
            FROM        MovieRating
            GROUP BY    user_id
        ) AS rated_counts
),
    ar AS(
        SELECT  movie_id, AVG(rating*1.0) AS avg_rating
        FROM    MovieRating
        WHERE   created_at LIKE '2020-02%'
        GROUP BY    movie_id
)--,
--     ranking_av AS (
--         SELECT  movie_id, avg_rating,
--                 RANK() OVER(ORDER BY avg_rating DESC) AS ranking
--         FROM    ar
-- )
-- SELECT  TOP 1 rc.user_id, rc.rated_movies, rc.rankings, u.name
SELECT results 
FROM (
    SELECT  TOP 1 u.name AS results
    FROM    rc
    JOIN    Users u ON u.user_id = rc.user_id
    WHERE   rankings = 1
    ORDER BY u.name ASC
) query_1

UNION ALL

-- SELECT  TOP 1  r.movie_id, r.avg_rating, r.ranking, m.title
SELECT results 
FROM (
    SELECT   TOP 1 m.title AS results
    FROM    ar AS r --ranking_av r
    JOIN    Movies m ON m.movie_id = r.movie_id
    ORDER BY    r.avg_rating DESC, m.title ASC
) query_2



