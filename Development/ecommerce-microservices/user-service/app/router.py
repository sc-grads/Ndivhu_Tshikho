from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import controller
from database import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = controller.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return controller.create_user(db, user)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = controller.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful", "email": user.email}
