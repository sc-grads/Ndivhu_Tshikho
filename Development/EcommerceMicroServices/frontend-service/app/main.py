from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Updated URLs to go through NGINX
USER_SERVICE_URL =  "http://nginx/api/users"
PRODUCT_SERVICE_URL = "http://user_product:8000"  # Updated to use Nginx service

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_user(request: Request, username: str = Form(...), password: str = Form(...)):
    data = {"username": username, "password": password}
    response = requests.post(f"{USER_SERVICE_URL}/login", json=data)
    
    if response.status_code == 200:
        return RedirectResponse(url="/products", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register_user(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    data = {"username": username, "email": email, "password": password}
    response = requests.post(f"{USER_SERVICE_URL}/register", json=data)
    
    if response.status_code == 201:
        return RedirectResponse(url="/login", status_code=303)
    else:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Registration failed"})

@app.get("/products")
async def list_products(request: Request):
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    
    if response.status_code == 200:
        products = response.json()
        return templates.TemplateResponse("product_list.html", {"request": request, "products": products})
    else:
        return templates.TemplateResponse("product_list.html", {"request": request, "products": [], "error": "Failed to fetch products"})
