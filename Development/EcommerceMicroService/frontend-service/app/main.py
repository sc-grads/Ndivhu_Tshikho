from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS to allow communication between services
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins during development, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Backend URLs going through Nginx
USER_SERVICE_URL = "http://nginx/api/users"  # Nginx will route to user-service

@app.get("/")
async def home(request: Request):
    """Render the homepage."""
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    """Render the login page."""
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_user(request: Request, username: str = Form(...), password: str = Form(...)):
    """Handle user login."""
    data = {"username": username, "password": password}
    response = requests.post(f"{USER_SERVICE_URL}/login", json=data)

    if response.status_code == 200:
        return RedirectResponse(url="/products", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/register")
async def register_page(request: Request):
    """Render the registration page."""
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register_user(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    """Handle user registration."""
    data = {"username": username, "email": email, "password": password}
    response = requests.post(f"{USER_SERVICE_URL}/register", json=data)

    if response.status_code == 201:
        return RedirectResponse(url="/login", status_code=303)
    else:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Registration failed"})
