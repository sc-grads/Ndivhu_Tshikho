from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from database import get_db
from controller.product_controller import create_product, get_products, update_product, delete_product

router = APIRouter()

@router.post("/store/products")
async def add_product(
    name: str, 
    description: str, 
    price: float, 
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    # Read the file content
    image_url = f"/store/static/{file.filename}"
    # Save the file
    file_location = f"static/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    
    return create_product(db, name, description, price, image_url)

@router.get("/store/products")  # Add leading "/"
def list_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.put("/store/products/{product_id}")
async def modify_product(
    product_id: int,
    name: str,
    description: str,
    price: float,
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    # Handle file upload similarly
    image_url = f"store/static/{file.filename}"
    file_location = f"/store/static/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    
    return update_product(db, product_id, name, description, price, image_url)

@router.delete("/store/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)
