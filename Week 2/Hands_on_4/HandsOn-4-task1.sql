-- Task 1 : Baseline Performance (Without Indexes)

--48. Display execution plan

EXPLAIN SELECT s.first_name, s.last_name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE s.enrollment_year = 2022;

-- Sample Output:
--
-- +----+-------------+-------------+--------+---------------+---------+---------+---------------------------+------+-------------+
-- | id | select_type | table       | type   | possible_keys | key     | key_len | ref                       | rows | Extra       |
-- +----+-------------+-------------+--------+---------------+---------+---------+---------------------------+------+-------------+
-- | 1  | SIMPLE      | students    | ALL    | NULL          | NULL    | NULL    | NULL                      | 8    | Using where |
-- | 1  | SIMPLE      | enrollments | ref    | student_id    | student_id | 4     | college_db.students.student_id | 12 |             |
-- | 1  | SIMPLE      | courses     | eq_ref | PRIMARY       | PRIMARY | 4       | college_db.enrollments.course_id | 1 |             |
-- +----+-------------+-------------+--------+---------------+---------+---------+---------------------------+------+-------------+

--49. Identify the table using full table scan

-- Observation:
-- The students table performs a full table scan (type = ALL)
-- because the enrollment_year column does not have an index.

--50. Estimated rows scanned

-- Estimated Rows:
-- students    : 8
-- enrollments : 12
-- courses     : 1

-- Conclusion:
-- As there is no index on enrollment_year, MySQL checks every row
-- in the students table before joining it with the other tables.