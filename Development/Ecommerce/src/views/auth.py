from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from controllers.auth_controller import create_user
from config import SessionLocal

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/register")
def register_view(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
def register(request: Request, username: str, email: str, password: str, db: Session = Depends(get_db)):
    create_user(db, username, email, password)
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/login")
def login_view(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
