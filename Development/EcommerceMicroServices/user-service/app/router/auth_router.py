from fastapi import APIRouter, HTTPException, Depends
import jwt
from sqlalchemy.orm import Session
from model.user import User
from model.schemas import UserCreate, UserLogin, UserResponse
from database import get_db
from passlib.context import CryptContext
from utils.auth_utils import admin_required, user_required  # Import role dependencies

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/auth/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db), role: str = "user"):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Create a JWT token for the new user
    access_token = jwt.encode(
        {"sub": new_user.email, "role": new_user.role},
        "your_secret_key",  # Replace with your actual secret key
        algorithm="HS256"
    )

    # Return the user details along with the access token
    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role,
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post("/auth/login", response_model=UserResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_record = db.query(User).filter(User.email == user.email).first()
    
    if user_record is None or not pwd_context.verify(user.password, user_record.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create token with user's role
    access_token = jwt.encode(
        {"sub": user_record.email, "role": user_record.role},
        "your_secret_key",
        algorithm="HS256"
    )

    # Return user info along with the access token
    return {
        "id": user_record.id,
        "username": user_record.username,
        "email": user_record.email,
        "role": user_record.role,
        "access_token": access_token,
        "token_type": "bearer"
    }

# Admin-only route
@router.get("auth/admin-only", dependencies=[Depends(admin_required)])
def product_management():
    return {"message": "Admin access granted!"}

# User or Admin route
@router.get("auth/user-only", dependencies=[Depends(user_required)])
def user_dashboard():
    return {"message": "User or Admin access granted!"}
