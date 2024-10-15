from fastapi import APIRouter, Depends, File, UploadFile, Form, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from controller import create_product, get_products, update_product, delete_product
import os

router = APIRouter()

# Ensure the 'images/' directory exists before saving any files
if not os.path.exists('images'):
    os.makedirs('images')

@router.post("/store/products")
async def add_product(
    name: str = Form(...), 
    description: str = Form(...), 
    price: float = Form(...), 
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    try:
        # Save the uploaded image file
        file_location = f"images/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        
        image_url = f"/images/{file.filename}"  # URL for accessing the image
        
        # Call controller to save product in the database
        return create_product(db, name, description, price, image_url)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving product: {str(e)}")

@router.get("/store/products")
def list_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.put("/store/products/{product_id}")
async def update_existing_product(
    product_id: int, 
    name: str = Form(...), 
    description: str = Form(...), 
    price: float = Form(...), 
    file: UploadFile = File(None),  # Optional file for updating image
    db: Session = Depends(get_db)
):
    try:
        image_url = None

        if file:
            # If a new file is uploaded, save it
            file_location = f"images/{file.filename}"
            with open(file_location, "wb") as f:
                f.write(file.file.read())
            image_url = f"/images/{file.filename}"
        
        # Call controller to update product in the database
        return update_product(db, product_id, name, description, price, image_url)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating product: {str(e)}")

@router.delete("/store/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)
