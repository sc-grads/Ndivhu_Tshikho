from fastapi import APIRouter, Depends, File, UploadFile, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from controllers.product_controller import create_product, get_products, get_product, update_product, delete_product
from database import get_db
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Route to list all products
@router.get("/products")
def list_products(request: Request, db: Session = Depends(get_db)):
    products = get_products(db)
    return templates.TemplateResponse("product.html", {"request": request, "products": products})

# Route to view details of a single product
@router.get("/product/{product_id}")
def view_product(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    return templates.TemplateResponse("product_detail.html", {"request": request, "product": product})

# Route to render the add product page
@router.get("/add_product")
def add_product_page(request: Request):
    return templates.TemplateResponse("add_product.html", {"request": request})

# Route to handle product addition
@router.post("/add_product")
async def add_product(
    request: Request, 
    name: str = Form(...), 
    description: str = Form(...), 
    price: float = Form(...), 
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    # Save the uploaded image
    file_location = f"static/images/{file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    image_url = f"/static/images/{file.filename}"

    # Create the product in the database
    create_product(db, name, description, price, image_url)
    return RedirectResponse(url="/products", status_code=303)

# Route to render the product update page
@router.get("/update_product/{product_id}")
def update_product_page(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    return templates.TemplateResponse("update_product.html", {"request": request, "product": product})

# Route to handle product update
@router.post("/update_product/{product_id}")
async def update_product_info(
    product_id: int, 
    request: Request, 
    name: str = Form(...), 
    description: str = Form(...), 
    price: float = Form(...), 
    file: UploadFile = File(None), 
    db: Session = Depends(get_db)
):
    # Fetch the existing product
    product = get_product(db, product_id)
    image_url = product.image_url

    # Update image if a new file is uploaded
    if file:
        file_location = f"static/images/{file.filename}"
        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        image_url = f"/static/images/{file.filename}"

    # Update product in the database
    updated_product = update_product(db, product_id, name, description, price, image_url)
    return RedirectResponse(url=f"/product/{updated_product.id}", status_code=303)

# Route to handle product deletion
@router.post("/delete_product/{product_id}")
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return RedirectResponse(url="/products", status_code=303)
