from pydantic import BaseModel, EmailStr
from typing import Optional, List

class CourseBase(BaseModel):
    name: str
    code: str
    credits: str
    department_id: int

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    class Config:
        from_attributes = True

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    department_id: int
    enrollment_year: int

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class config:
        from_attributes = True