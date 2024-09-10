from sqlalchemy.orm import Session
from models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(db: Session, username: str, email: str, password: str):
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
