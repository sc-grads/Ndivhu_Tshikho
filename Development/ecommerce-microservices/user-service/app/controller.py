from sqlalchemy.orm import Session
import model, schemas
from utils import hash_password, verify_password

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = model.User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
