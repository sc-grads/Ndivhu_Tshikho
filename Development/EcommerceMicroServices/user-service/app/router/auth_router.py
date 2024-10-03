from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from database import get_db
from controller.auth_controller import create_user, get_user
from passlib.context import CryptContext

router = APIRouter()

# Setup password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pydantic models for validation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post("/auth/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = get_user(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = pwd_context.hash(user.password)
    
    # Create the user
    return create_user(db, user.username, user.email, hashed_password)

@router.post("/auth/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Fetch user by email
    user_record = get_user(db, user.email)
    if user_record is None or not pwd_context.verify(user.password, user_record.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful!"}
