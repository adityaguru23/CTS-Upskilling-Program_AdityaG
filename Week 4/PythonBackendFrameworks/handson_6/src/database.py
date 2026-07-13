db_courses = []
db_students = []
db_enrollments = []

async def get_db():
    yield {"courses": db_courses, "students": db_students, "enrollments": db_enrollments}