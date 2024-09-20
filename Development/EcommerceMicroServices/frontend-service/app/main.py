from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

USER_SERVICE_URL = "http://127.0.0.1:8001"  # Adjust accordingly
PRODUCT_SERVICE_URL = "http://127.0.0.1:8002"  # Adjust accordingly

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_user(request: Request, username: str = Form(...), password: str = Form(...)):
    data = {"username": username, "password": password}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/api/users/login", json=data)
    if response.status_code == 200:
        return templates.TemplateResponse("product_list.html", {"request": request, "products": response.json()})
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register_user(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    data = {"username": username, "email": email, "password": password}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/api/users/register", json=data)
    if response.status_code == 201:
        return RedirectResponse(url="/login", status_code=303)
    return templates.TemplateResponse("register.html", {"request": request, "error": "Registration failed"})

@app.get("/products")
async def list_products(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_SERVICE_URL}/api/products")
    return templates.TemplateResponse("product_list.html", {"request": request, "products": response.json()})
