from sqlalchemy.orm import Session
from model.user import User
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, username: str, email: str, password: str, role: str = "user"):
    hashed_password = hash_password(password)
    user = User(username=username, email=email, password=hashed_password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
