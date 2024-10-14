# src/routers/cart_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.cart import CartItem
from database import get_db

router = APIRouter()

@router.post("/cart/")
async def add_to_cart(product_id: int, quantity: int, db: Session = Depends(get_db)):
    # Logic to add product to the cart
    cart_item = CartItem(product_id=product_id, quantity=quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.get("/cart/")
async def get_cart(db: Session = Depends(get_db)):
    return db.query(CartItem).all()

@router.put("/cart/{item_id}")
async def update_cart_item(item_id: int, quantity: int, db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item.quantity = quantity
    db.commit()
    return item

@router.delete("/cart/{item_id}")
async def remove_cart_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"detail": "Item removed from cart"}
