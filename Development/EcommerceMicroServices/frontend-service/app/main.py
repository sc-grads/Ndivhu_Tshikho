from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Serve static files (like CSS and JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


