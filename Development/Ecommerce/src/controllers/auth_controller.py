from sqlalchemy.orm import Session
from models.user import User
from passlib.context import CryptContext
import logging

# Setup password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Setup logging
logger = logging.getLogger(__name__)

def register_user(db: Session, username: str, email: str, password: str):
    hashed_password = pwd_context.hash(password)
    try:
        # Check if the username or email already exists
        if db.query(User).filter(User.username == username).first():
            raise ValueError("Username already exists")
        if db.query(User).filter(User.email == email).first():
            raise ValueError("Email already exists")

        # Create a new user and add it to the database
        user = User(username=username, email=email, password=hashed_password)
        db.add(user)
        db.commit()
        logger.info(f"User registered: {username}")
        return user
    except ValueError as ve:
        logger.warning(f"Validation error during registration for {username}: {ve}")
        raise
    except Exception as e:
        db.rollback()  # Rollback the transaction on error
        logger.error(f"Error registering user {username}: {e}")
        raise

def login_user(db: Session, username: str, password: str):
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and pwd_context.verify(password, user.password):
            logger.info(f"User logged in: {username}")
            return user
        else:
            logger.warning(f"Failed login attempt for user: {username}")
            return None
    except Exception as e:
        logger.error(f"Error logging in user {username}: {e}")
        raise
