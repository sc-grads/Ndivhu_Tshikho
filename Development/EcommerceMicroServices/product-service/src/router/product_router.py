from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.product_controller import create_product, get_products, update_product, delete_product

router = APIRouter()

@router.post("/products")
def add_product(name: str, description: str, price: float, db: Session = Depends(get_db)):
    return create_product(db, name, description, price)

@router.get("/products")
def list_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.put("/products/{product_id}")
def modify_product(product_id: int, name: str, description: str, price: float, db: Session = Depends(get_db)):
    return update_product(db, product_id, name, description, price)

@router.delete("/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)
