-- Task 1

INSERT INTO departments (dept_name, hod_name, budget) VALUES ('Computer Science', 'Dr. Ramesh Kumar', 850000.00), ('Electronics', 'Dr. Priya Nair', 620000.00), ('Mechanical', 'Dr. Suresh Iyer', 540000.00);

INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES ('Arjun', 'Mehta', 'arjun.mehta@college.edu', '2003-04-12', 1, 2022), ('Priya', 'Suresh', 'priya.suresh@college.edu', '2003-07-25', 1, 2022), ('Rohan', 'Verma', 'rohan.verma@college.edu', '2002-11-08', 2, 2021), ('Sneha', 'Patel', 'sneha.patel@college.edu', '2004-01-30', 3, 2023), ('Vikram', 'Das', 'vikram.das@college.edu', '2003-09-14', 1, 2022);

INSERT INTO courses (course_name, course_code, credits, department_id) VALUES ('Data Structures', 'CS101', 4, 1), ('Database Systems', 'CS102', 3, 1), ('Circuit Theory', 'EC101', 3, 2);

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (1, 1, '2022-07-01', 'A'), (1, 2, '2022-07-01', 'B'), (2, 1, '2022-07-01', 'A'), (3, 3, '2021-07-01', 'B'), (4, 3, '2023-07-01', NULL);

INSERT INTO professors (prof_name, email, department_id, salary) VALUES ('Dr. Anand Krishnan', 'anand.k@college.edu', 1, 95000.00), ('Dr. Meena Pillai', 'meena.p@college.edu', 1, 88000.00), ('Dr. Sunil Rajan', 'sunil.r@college.edu', 2, 82000.00);

INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES ('Karna', 'Suresh', 'karna.suresh@college.edu', '2003-07-25', 1, 2022);

SELECT COUNT(*) AS Total_Students FROM students;

UPDATE enrollments SET grade='B' WHERE student_id=2 AND course_id=1;

SELECT * FROM enrollments WHERE student_id=2 AND course_id=1;

DELETE FROM enrollments WHERE grade IS NULL;

SELECT COUNT(*) AS Total FROM enrollments;

SELECT * FROM enrollments;


-- Task 2

SELECT * FROM students WHERE enrollment_year=2022 ORDER BY first_name;

SELECT * FROM courses WHERE credits>=3 ORDER BY course_name;

SELECT * FROM professors WHERE salary BETWEEN 80000 AND 95000;

SELECT * FROM students WHERE email LIKE '%@college.edu';

SELECT enrollment_year, COUNT(*) AS students_count FROM students GROUP BY enrollment_year;


-- Task 3

SELECT CONCAT(s.first_name,' ',s.last_name) AS student_name, d.dept_name FROM students s JOIN departments d ON s.department_id=d.department_id;

SELECT e.enrollment_date, CONCAT(s.first_name,' ',s.last_name) AS student_name, c.course_name FROM enrollments e JOIN students s ON e.student_id=s.student_id JOIN courses c ON e.course_id=c.course_id;

SELECT s.* FROM students s LEFT JOIN enrollments e ON s.student_id=e.student_id WHERE e.student_id IS NULL;

SELECT c.course_name, COUNT(e.student_id) AS enrolled_students FROM courses c LEFT JOIN enrollments e ON c.course_id=e.course_id GROUP BY c.course_name;

SELECT d.dept_name, p.prof_name, p.salary FROM departments d LEFT JOIN professors p ON d.department_id=p.department_id;


-- Task 4

SELECT c.course_name, COUNT(e.student_id) AS total_enrollments FROM courses c LEFT JOIN enrollments e ON c.course_id=e.course_id GROUP BY c.course_name;

SELECT d.dept_name, ROUND(AVG(p.salary),2) AS avg_salary FROM professors p JOIN departments d ON p.department_id=d.department_id GROUP BY d.dept_name;

SELECT * FROM departments WHERE budget>600000;

SELECT e.grade, COUNT(*) AS grade_count FROM courses c JOIN enrollments e ON c.course_id=e.course_id WHERE c.course_code='CS101' GROUP BY e.grade;

SELECT d.dept_name FROM departments d JOIN students s ON d.department_id=s.department_id GROUP BY d.dept_name HAVING COUNT(s.student_id)>1;