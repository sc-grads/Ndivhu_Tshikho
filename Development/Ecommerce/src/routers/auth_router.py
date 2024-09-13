from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user import User
from database import get_db
import logging

# Setup logging
logger = logging.getLogger(__name__)

# Setup FastAPI Router and Jinja2 Templates
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Setup password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/register")
async def get_register(request: Request):
    logger.info("Accessing registration page")
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def post_register(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(password)
    try:
        user = User(username=username, email=email, password=hashed_password)
        db.add(user)
        db.commit()
        logger.info(f"User registered: {username}")
        return RedirectResponse(url="/login", status_code=303)
    except Exception as e:
        db.rollback()  # Rollback the transaction on error
        logger.error(f"Error registering user {username}: {e}")
        return templates.TemplateResponse("register.html", {"request": request, "message": "Registration failed"})

@router.get("/login")
async def get_login(request: Request):
    logger.info("Accessing login page")
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def post_login(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == email).first()
        if user and pwd_context.verify(password, user.password):
            logger.info(f"User logged in: {email}")
            # Set session or token here
            return RedirectResponse(url="/products", status_code=303)
        else:
            logger.warning(f"Failed login attempt for user: {email}")
            return templates.TemplateResponse("login.html", {"request": request, "message": "Invalid credentials"})
    except Exception as e:
        logger.error(f"Error logging in user {email}: {e}")
        return templates.TemplateResponse("login.html", {"request": request, "message": "Login failed"})
