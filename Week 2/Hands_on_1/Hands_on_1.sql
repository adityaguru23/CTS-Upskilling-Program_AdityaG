-- Task 1

-- All tables have been created successfully with the required constraints.
-- The table definitions are available in the DBschema.sql file.

-- Display the structure of each table
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE professors;
DESCRIBE enrollments;


-- Task 2 : Normalization Verification

-- First Normal Form (1NF)
-- Every table contains atomic values and there are no repeating columns.
-- If multiple phone numbers or email addresses were stored in one column,
-- it would violate 1NF. Such values should be moved to a separate table.
-- Conclusion: Database satisfies 1NF.

-- Second Normal Form (2NF)
-- Every table has a single primary key.
-- Since there are no composite primary keys, partial dependency is not possible.
-- Conclusion: Database satisfies 2NF.

-- Third Normal Form (3NF)
-- Every non-key attribute depends only on its respective primary key.
-- There are no transitive dependencies between non-key attributes.
-- Conclusion: Database satisfies 3NF.


-- Task 3

-- Add a new column to students
ALTER TABLE students
ADD phone_number VARCHAR(15);

-- Add maximum seat capacity to courses
ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

-- Restrict grade values
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F'));

-- Rename HOD column
ALTER TABLE departments
CHANGE hod_name head_of_dept VARCHAR(100);

-- Remove phone number column
ALTER TABLE students
DROP COLUMN phone_number;


-- View updated table structures
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;