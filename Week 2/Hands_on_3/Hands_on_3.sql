-- Task 1

--35. Students enrolled in more courses than the average

SELECT s.student_id,s.first_name,s.last_name,COUNT(*) AS total_courses
FROM students s
JOIN enrollments e ON s.student_id=e.student_id
GROUP BY s.student_id,s.first_name,s.last_name
HAVING COUNT(*) >
(
SELECT AVG(course_total)
FROM
(
SELECT COUNT(*) AS course_total
FROM enrollments
GROUP BY student_id
) t
);

--36. Courses where every enrolled student received grade A

SELECT c.course_name
FROM courses c
WHERE NOT EXISTS
(
SELECT *
FROM enrollments e
WHERE e.course_id=c.course_id
AND e.grade<>'A'
);

--37. Highest paid professor in each department

SELECT p.professor_id,p.prof_name,p.salary,d.dept_name
FROM professors p
JOIN departments d ON p.department_id=d.department_id
WHERE p.salary=
(
SELECT MAX(salary)
FROM professors
WHERE department_id=p.department_id
);

--38. Departments with average salary above 85000

SELECT d.dept_name,a.avg_salary
FROM
(
SELECT department_id,AVG(salary) AS avg_salary
FROM professors
GROUP BY department_id
) a
JOIN departments d
ON a.department_id=d.department_id
WHERE a.avg_salary>85000;


-- Task 2

--39. Student enrollment summary view

CREATE OR REPLACE VIEW vw_student_enrollment_summary AS
SELECT s.student_id,CONCAT(s.first_name,' ',s.last_name) AS student_name,d.dept_name,COUNT(e.course_id) AS total_courses,
ROUND(AVG(CASE WHEN e.grade='A' THEN 4 WHEN e.grade='B' THEN 3 WHEN e.grade='C' THEN 2 WHEN e.grade='D' THEN 1 WHEN e.grade='F' THEN 0 END),2) AS gpa
FROM students s
JOIN departments d ON s.department_id=d.department_id
LEFT JOIN enrollments e ON s.student_id=e.student_id
GROUP BY s.student_id,s.first_name,s.last_name,d.dept_name;

--40. Course statistics view

CREATE OR REPLACE VIEW vw_course_stats AS
SELECT c.course_name,c.course_code,COUNT(e.enrollment_id) AS total_enrollments,
ROUND(AVG(CASE WHEN e.grade='A' THEN 4 WHEN e.grade='B' THEN 3 WHEN e.grade='C' THEN 2 WHEN e.grade='D' THEN 1 WHEN e.grade='F' THEN 0 END),2) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e ON c.course_id=e.course_id
GROUP BY c.course_name,c.course_code;

--41. Students having GPA greater than 3

SELECT * FROM vw_student_enrollment_summary WHERE gpa>3;

--42. Update through the view

UPDATE vw_student_enrollment_summary
SET student_name='Updated Student'
WHERE student_id=1;

-- This update may fail because the view contains multiple joined tables.

--43. Recreate view using CHECK OPTION

DROP VIEW IF EXISTS vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT student_id,first_name,last_name,email,enrollment_year
FROM students
WHERE enrollment_year>=2022
WITH CHECK OPTION;


-- Task 3

--44. Function to enroll a student

CREATE OR REPLACE FUNCTION fn_enroll_student(p_student_id INT,p_course_id INT,p_enrollment_date DATE)
RETURNS VOID
LANGUAGE plpgsql
AS
$$
BEGIN
IF EXISTS(SELECT 1 FROM enrollments WHERE student_id=p_student_id AND course_id=p_course_id) THEN
RAISE EXCEPTION 'Student already enrolled.';
END IF;

INSERT INTO enrollments(student_id,course_id,enrollment_date)
VALUES(p_student_id,p_course_id,p_enrollment_date);
END;
$$;

-- Test

SELECT fn_enroll_student(2,3,CURRENT_DATE);

--45. Department transfer log table

CREATE TABLE department_transfer_log
(
log_id SERIAL PRIMARY KEY,
student_id INT,
old_department INT,
new_department INT,
transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--46. Student department transfer

BEGIN;

UPDATE students
SET department_id=2
WHERE student_id=1;

INSERT INTO department_transfer_log(student_id,old_department,new_department)
VALUES(1,1,2);

COMMIT;

--47. SAVEPOINT demonstration

BEGIN;

INSERT INTO enrollments(student_id,course_id,enrollment_date)
VALUES(3,2,CURRENT_DATE);

SAVEPOINT sp1;

INSERT INTO enrollments(student_id,course_id,enrollment_date)
VALUES(3,2,CURRENT_DATE);

ROLLBACK TO SAVEPOINT sp1;

COMMIT;

SELECT * FROM enrollments WHERE student_id=3 AND course_id=2;