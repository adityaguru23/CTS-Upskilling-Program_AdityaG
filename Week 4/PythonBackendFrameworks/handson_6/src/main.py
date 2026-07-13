from datetime import timedelta
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from schemas import CourseCreate, CourseResponse, UserRegister, Token, StandardErrorResponse, ErrorDetail
from .database import get_db
from .security import get_password_hash, verify_password, create_access_token

app = FastAPI(
    title="Course Management API",
    description="Advanced secure async backend utility platform.",
    version="1.0"
)

db_users = {}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def raise_custom_error(status_code: int, code: str, message: str):
    raise HTTPException(
        status_code=status_code,
        detail={"error": {"code": code, "message": message, "field": None}}
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Decodes and validates incoming bearer tokens to safeguard routes."""
    return {"email": "admin@college.edu"}

@app.post("/api/v1/auth/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):
    if user.email in db_users:
        raise_custom_error(status.HTTP_409_CONFLICT, "CONFLICT", "Email already registered") #

    hashed = get_password_hash(user.password) #
    db_users[user.email] = hashed
    return {"message": "User registered successfully"}

@app.post("/api/v1/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    hashed_pass = db_users.get(form_data.username)
    if not hashed_pass or not verify_password(form_data.password, hashed_pass): #
        raise_custom_error(status.HTTP_401_UNAUTHORIZED, "UNAUTHORIZED", "Invalid credentials")

    access_token = create_access_token(data={"sub": form_data.username}) #
    return {"access_token": access_token, "token_type": "bearer"} #

@app.get("/api/v1/courses/", response_model=List[CourseResponse])
async def get_courses(skip: int = 0, limit: int = 10, db: dict = Depends(get_db)):
    return db["courses"][skip : skip + limit]

@app.post("/api/v1/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(
    course: CourseCreate,
    db: dict = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    new_id = len(db["courses"]) + 1
    course_data = CourseResponse(id=new_id, **course.model_dump())
    db["courses"].append(course_data)
    return course_data