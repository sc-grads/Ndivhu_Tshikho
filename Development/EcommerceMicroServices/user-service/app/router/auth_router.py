# src/routers/auth_router.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from model.user import User
from model.schemas import UserCreate, UserLogin, UserResponse
from database import get_db
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/auth/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = pwd_context.hash(user.password)

    # Create a new user instance
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
    )

    # Add the user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/auth/login", response_model=UserResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Retrieve the user from the database
    user_record = db.query(User).filter(User.email == user.email).first()
    
    # Check if the user exists
    if user_record is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Verify the password
    if not pwd_context.verify(user.password, user_record.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Return user information (excluding password)
    return {"id": user_record.id, "username": user_record.username, "email": user_record.email}