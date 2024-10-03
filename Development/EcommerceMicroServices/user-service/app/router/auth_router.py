from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from controller.auth_controller import create_user, get_user
from passlib.context import CryptContext

router = APIRouter()

# Setup password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, email, password)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = get_user(db, email)
    if user is None or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful!"}
