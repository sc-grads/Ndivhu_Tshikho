from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from models import user as user_model

def create_user(db: Session, username: str, email: str, password: str):
    hashed_password = bcrypt.hash(password)
    new_user = user_model.User(username=username, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and bcrypt.verify(password, user.password):
        return user
    return False
