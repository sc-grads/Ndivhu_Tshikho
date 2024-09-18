from fastapi import APIRouter, Depends, File, UploadFile, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from controllers.product_controller import create_product, get_products, get_product, update_product, delete_product
from database import get_db
import logging
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Set up a logger for product actions
product_logger = logging.getLogger('product')

@router.get("/products")
def list_products(request: Request, db: Session = Depends(get_db)):
    products = get_products(db)
    return templates.TemplateResponse("product.html", {"request": request, "products": products})

@router.get("/product/{product_id}")
def view_product(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    return templates.TemplateResponse("product_detail.html", {"request": request, "product": product})

@router.get("/add_product")
def add_product_page(request: Request):
    return templates.TemplateResponse("add_product.html", {"request": request})

@router.post("/add_product")
async def add_product(request: Request, name: str = Form(...), description: str = Form(...), price: float = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"static/images/{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    image_url = f"/static/images/{file.filename}"
    create_product(db, name, description, price, image_url)
    
    product_logger.info(f'Added product: {name}, {description}, {price}, {image_url}')
    
    return RedirectResponse(url="/products", status_code=303)

@router.get("/update_product/{product_id}")
def update_product_page(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    return templates.TemplateResponse("update_product.html", {"request": request, "product": product})

@router.post("/update_product/{product_id}")
async def update_product_info(product_id: int, request: Request, name: str = Form(...), description: str = Form(...), price: float = Form(...), file: UploadFile = File(None), db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    image_url = product.image_url
    if file:
        file_location = f"static/images/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        image_url = f"/static/images/{file.filename}"
    
    updated_product = update_product(db, product_id, name, description, price, image_url)
    
    product_logger.info(f'Updated product ID {product_id}: {name}, {description}, {price}, {image_url}')
    
    return RedirectResponse(url=f"/product/{updated_product.id}", status_code=303)

@router.post("/delete_product/{product_id}")
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    
    product_logger.info(f'Deleted product ID {product_id}')
    
    return RedirectResponse(url="/products", status_code=303)
