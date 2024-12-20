# app/router/cart_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controller.cart_controller import add_to_cart, get_cart_items, update_cart_item, remove_cart_item
from database import get_db

router = APIRouter()

@router.post("/cart")
def add_product_to_cart(product_id: int, quantity: int, db: Session = Depends(get_db)):
    return add_to_cart(db, product_id, quantity)

@router.get("/cart")
def list_cart_items(db: Session = Depends(get_db)):
    return get_cart_items(db)

@router.put("/cart/{cart_id}")
def update_cart_item_quantity(cart_id: int, quantity: int, db: Session = Depends(get_db)):
    return update_cart_item(db, cart_id, quantity)

@router.delete("/cart/{cart_id}")
def delete_cart_item(cart_id: int, db: Session = Depends(get_db)):
    return remove_cart_item(db, cart_id)
