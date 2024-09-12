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
async def post_login(request: Request, username: str = Form(...), password: str = Form(...)):
    db: Session = next(get_db())
    try:
        user = login_user(db, username, password)
        if user:
            logger.info(f"User logged in: {username}")
            # Set session or token here if applicable
            return RedirectResponse(url="/products", status_code=303)
        else:
            logger.warning(f"Failed login attempt for user: {username}")
            return templates.TemplateResponse("login.html", {"request": request, "message": "Invalid credentials"})
    except Exception as e:
        logger.error(f"Error logging in user {username}: {e}")
        return templates.TemplateResponse("login.html", {"request": request, "message": "Login failed"})
