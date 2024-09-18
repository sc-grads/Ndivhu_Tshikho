from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controller.auth_controller import create_user, authenticate_user

router = APIRouter()

@router.post("/register")
def register_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, email, password)

@router.post("/login")
def login_user(username: str, password: str, db: Session = Depends(get_db)):
    return authenticate_user(db, username, password)
