from sqlite3 import IntegrityError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db  # Assuming you have a function to get the database session
from user_model import User  # Import your user model here
from pydantic import BaseModel, EmailStr

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

@router.post("/register", response_model=dict)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Create a new user instance
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)  # Add the user to the session
    try:
        db.commit()  # Commit the transaction
        return {"message": "User registered successfully"}
    except IntegrityError:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=400, detail="Username or email already exists")
    except Exception as e:
        db.rollback()
        print(f"Error registering user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
