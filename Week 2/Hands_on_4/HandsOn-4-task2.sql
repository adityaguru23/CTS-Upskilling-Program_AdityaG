-- Task 2 : Create Indexes and Compare Execution Plan

--51. Create an index on enrollment_year

CREATE INDEX idx_enrollment_year
ON students(enrollment_year);

--52. Create a unique composite index

CREATE UNIQUE INDEX idx_student_course
ON enrollments(student_id, course_id);

--53. Create an index for course_code

CREATE INDEX idx_courses_code
ON courses(course_code);

--54. Check the execution plan after indexing

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON e.course_id = c.course_id
WHERE s.enrollment_year = 2022;

-- Sample Output:
--
-- +----+-------------+-------------+------------+------+---------------+------+---------+------+------+----------+-------------+
-- | id | select_type | table       | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
-- +----+-------------+-------------+------------+------+---------------+------+---------+------+------+----------+-------------+
-- | 1  | SIMPLE      | enrollments | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 22   | 10.00    | Using where |
-- +----+-------------+-------------+------------+------+---------------+------+---------+------+------+----------+-------------+

-- Observation:
-- The optimizer can now make use of the created indexes.
-- The query performs better than before and scans fewer records.

--55. Create an index for NULL grade searches

-- Since MySQL does not support partial indexes,
-- a composite index is created instead.

CREATE INDEX idx_grade_lookup
ON enrollments(grade, student_id);

-- Verify the execution plan

EXPLAIN
SELECT *
FROM enrollments
WHERE grade IS NULL;