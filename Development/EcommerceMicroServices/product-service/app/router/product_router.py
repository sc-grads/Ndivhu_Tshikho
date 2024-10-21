from fastapi import APIRouter, Depends, File, Form, UploadFile, HTTPException, Request
from sqlalchemy.orm import Session
from model.product import Product
from database import get_db
from controller.product_controller import create_product, get_products, update_product, delete_product
import os

router = APIRouter()

UPLOAD_DIR = "images"

# Ensure the directory exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/store/products")
async def add_product(
    name: str = Form(...),  # Form data for non-file fields
    description: str = Form(...),
    price: float = Form(...),
    file: UploadFile = File(...),  # File upload
    db: Session = Depends(get_db)
):
    try:
        # Save the file to disk
        image_url = f"/{UPLOAD_DIR}/{file.filename}"
        file_location = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_location, "wb") as f:
            f.write(await file.read())  # Save uploaded file

        # Create the product using the controller logic
        new_product = create_product(db, name, description, price, image_url)
        return new_product
    except Exception as e:
        # Log the request body and error for debugging
        print(f"Error occurred: {e}")
        print(f"Request body: {await Request.form()}")
        raise HTTPException(status_code=400, detail=str(e))

        
@router.get("/store/products")
def list_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/store/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/store/products/{product_id}")
async def update_product_endpoint(
    product_id: int,
    name: str,
    description: str,
    price: float,
    file: UploadFile = File(None),  # File is optional in case there's no new file
    db: Session = Depends(get_db)
):
    image_url = None
    if file:
        # If a new file is uploaded, save the new file
        image_url = f"/{UPLOAD_DIR}/{file.filename}"
        file_location = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_location, "wb") as f:
            f.write(await file.read())  # Use await for asynchronous file handling

    # Update the product details with or without a new image
    updated_product = update_product(db, product_id, name, description, price, image_url)
    return updated_product

@router.delete("/store/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"detail": "Product deleted successfully"}
