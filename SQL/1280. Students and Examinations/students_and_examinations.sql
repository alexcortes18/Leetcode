/* Write your T-SQL query statement below */

SELECT students.student_id, students.student_name, subjects.subject_name,
COALESCE(examinations.attended_exams,0) as attended_exams
FROM Students AS students
CROSS JOIN Subjects AS subjects
LEFT JOIN (
    SELECT student_id, subject_name, 
    COUNT(*) attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) AS examinations ON students.student_id = examinations.student_id
AND subjects.subject_name = examinations.subject_name
-- ON examinations.subject_name = subjects.subject_name
ORDER BY students.student_id, subjects.subject_name

