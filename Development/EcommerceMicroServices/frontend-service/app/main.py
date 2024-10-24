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

@app.get("/products")
def product_page(request: Request):
    return templates.TemplateResponse("product.html", {"request": request})

@app.get("/add-product")
def add_product_page(request: Request):
    return templates.TemplateResponse("add-product.html", {"request": request})

@app.get("/edit-product")
def edit_product_page(request: Request):
    return templates.TemplateResponse("edit-product.html", {"request": request}) 

@app.get("/shop")
def shop_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})  

@app.get("/profile")
def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})



