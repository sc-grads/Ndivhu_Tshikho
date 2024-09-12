from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.auth_controller import create_user, authenticate_user
from database import get_db

router = APIRouter()

@router.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = create_user(db, username, email, password)
    return {"message": "User created successfully", "user": user.username}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Logged in successfully", "user": user.username}
