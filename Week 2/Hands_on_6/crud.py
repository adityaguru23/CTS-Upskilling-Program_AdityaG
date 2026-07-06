from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from models import Department, Student, Course, Enrollment

DATABASE_URL = "mysql+pymysql://root:root@localhost/college_dbs_orm"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
db = Session()


# Task 2: CRUD Operations

# 80. Start Session

print("Database Session Started")


# 81. Insert Departments

dept1 = Department(dept_name="Computer Science", hod_name="Dr. Ramesh Kumar", budget=850000)
dept2 = Department(dept_name="Electronics", hod_name="Dr. Priya Nair", budget=620000)
dept3 = Department(dept_name="Mechanical", hod_name="Dr. Suresh Iyer", budget=540000)

db.add_all([dept1, dept2, dept3])
db.commit()

print("Departments Added")


# Insert Students

student_list = [
    Student(first_name="Arjun", last_name="Mehta", email="arjun@gmail.com", enrollment_year=2022, department=dept1),
    Student(first_name="Priya", last_name="Suresh", email="priya@gmail.com", enrollment_year=2022, department=dept1),
    Student(first_name="Rohan", last_name="Verma", email="rohan@gmail.com", enrollment_year=2021, department=dept2),
    Student(first_name="Sneha", last_name="Patel", email="sneha@gmail.com", enrollment_year=2023, department=dept3)
]

db.add_all(student_list)
db.commit()

print("Students Added")


# 82. Insert Courses

courses = [
    Course(course_name="Data Structures", course_code="CS101", credits=4, department=dept1),
    Course(course_name="Database Systems", course_code="CS102", credits=3, department=dept1),
    Course(course_name="Circuit Theory", course_code="EC101", credits=3, department=dept2)
]

db.add_all(courses)
db.commit()

print("Courses Added")


# Insert Enrollments

records = [
    Enrollment(student=student_list[0], course=courses[0]),
    Enrollment(student=student_list[1], course=courses[0]),
    Enrollment(student=student_list[2], course=courses[2])
]

db.add_all(records)
db.commit()

print("Enrollments Added")


# 83. Display Computer Science Students

print("\nComputer Science Students\n")

students = db.query(Student).join(Department).filter(Department.dept_name == "Computer Science").all()

for s in students:
    print(s.student_id, s.first_name, s.last_name)


# 84. Display Enrollment Details

print("\nEnrollment Details\n")

for e in db.query(Enrollment).all():
    print(e.student.first_name, "->", e.course.course_name)


# 85. Update Student

student = db.query(Student).filter_by(email="arjun@gmail.com").first()

if student:
    student.enrollment_year = 2024
    db.commit()
    print("\nStudent Record Updated")

updated = db.query(Student).filter_by(email="arjun@gmail.com").first()
print(updated.first_name, updated.enrollment_year)


# 86. Delete One Enrollment

record = db.query(Enrollment).first()

if record:
    db.delete(record)
    db.commit()
    print("\nEnrollment Removed")

print("\nRemaining Enrollments")

for e in db.query(Enrollment).all():
    print(e.enrollment_id, e.student.first_name, e.course.course_name)


# Task 3: Eager Loading

# 87. N+1 Problem

print("\nWithout joinedload()\n")

records = db.query(Enrollment).all()

for r in records:
    print(r.student.first_name, "-", r.course.course_name)

print("\nObservation:")
print("Multiple SQL queries are executed due to lazy loading.")


# 88. Fix Using joinedload()

print("\nWith joinedload()\n")

records = (
    db.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for r in records:
    print(r.student.first_name, "-", r.course.course_name)


# 89. Query Observation

print("\nObservation:")
print("joinedload() fetches related data using one JOIN query.")


# 90. Comparison

print("\nComparison")
print("-----------------------------")
print("Without joinedload()")
print("- Multiple SQL queries")
print("- N+1 Problem")

print("\nWith joinedload()")
print("- Single JOIN query")
print("- Better Performance")


# 91. Django ORM Equivalent

print("\nDjango ORM Equivalent")
print("Enrollment.objects.select_related('student','course').all()")

db.close()

print("\nDatabase Session Closed")