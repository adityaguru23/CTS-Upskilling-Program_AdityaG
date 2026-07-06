from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    Numeric,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import declarative_base, relationship

# Database Configuration

DATABASE_URL = "mysql+pymysql://root:root@localhost/college_dbs_orm"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


# Department Model

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=False)
    hod_name = Column(String(100))
    budget = Column(Numeric(12, 2))

    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")
    professors = relationship("Professor", back_populates="department")


# Student Model

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date)
    enrollment_year = Column(Integer)
    is_active = Column(Boolean, default=True)

    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


# Course Model

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(150), nullable=False)
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)

    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    schedules = relationship("CourseSchedule", back_populates="course")


# Course Schedule Model

class CourseSchedule(Base):
    __tablename__ = "course_schedules"

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    day_of_week = Column(String(20))
    start_time = Column(String(10))
    end_time = Column(String(10))

    course = relationship("Course", back_populates="schedules")


# Enrollment Model

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


# Professor Model

class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    salary = Column(Numeric(10, 2))

    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="professors")


# Create Tables

if __name__ == "__main__":

    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully.")