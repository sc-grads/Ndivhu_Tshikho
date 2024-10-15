from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
import schemas
import controller
from database import get_db
import model

router = APIRouter()

@router.post("/auth/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = controller.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return controller.create_user(db, user)
    return {"message": "Login successful", "email": user.email}

@router.post("/auth/login", response_model=schemas.UserResponse)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    # Retrieve the user from the database
    user_record = db.query(model.User).filter(model.User.email == user.email).first()
    
    # Check if the user exists
    if user_record is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Verify the password
    if not controller.authenticate_user(db, user.email, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Return user information (excluding password)
    return {"id": user_record.id, "username": user_record.username, "email": user_record.email}
