# app/router/product_router.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from utils.jwt_utils import decode_token  # Import the decoding function
from database import get_db
from model.product import Product
from controller.product_controller import create_product, get_products, update_product, delete_product
from model.schemas import ProductResponse, ProductCreate  # Ensure you have the appropriate schemas

router = APIRouter()

@router.post("/store/products", response_model=ProductResponse)
async def add_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    file: UploadFile = File(...),
    token: str = Depends(decode_token),  # Decode JWT here
    db: Session = Depends(get_db),
):
    if token.role != "admin":  # Check if user is admin
        raise HTTPException(status_code=403, detail="Operation not permitted")
    
    # Call the create_product function, ensuring it returns a ProductResponse
    product = await create_product(db, name, description, price, file)  # Assume create_product handles the file upload
    return product  # Ensure this returns an instance of ProductResponse

@router.put("/store/products/{product_id}", response_model=ProductResponse)
async def update_product_endpoint(
    product_id: int,
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    file: UploadFile = File(None),
    token: str = Depends(decode_token),
    db: Session = Depends(get_db),
):
    if token.role != "admin":
        raise HTTPException(status_code=403, detail="Operation not permitted")
    
    # Call the update_product function, ensuring it returns a ProductResponse
    updated_product = await update_product(db, product_id, name, description, price, file)  # Assume update_product handles the file upload
    return updated_product  # Ensure this returns an instance of ProductResponse

@router.delete("/store/products/{product_id}", response_model=dict)
def remove_product(
    product_id: int,
    token: str = Depends(decode_token),
    db: Session = Depends(get_db),
):
    if token.role != "admin":
        raise HTTPException(status_code=403, detail="Operation not permitted")
    
    delete_product(db, product_id)
    return {"detail": "Product deleted successfully"}
