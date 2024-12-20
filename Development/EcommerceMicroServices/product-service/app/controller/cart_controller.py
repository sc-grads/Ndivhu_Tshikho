# app/controller/cart_controller.py
from sqlalchemy.orm import Session
from model.cart import Cart
from model.product import Product
from fastapi import HTTPException

def add_to_cart(db: Session, product_id: int, quantity: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    total_price = product.price * quantity
    cart_item = Cart(product_id=product_id, quantity=quantity, total_price=total_price)

    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

def get_cart_items(db: Session):
    return db.query(Cart).all()

def update_cart_item(db: Session, cart_id: int, quantity: int):
    cart_item = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    cart_item.quantity = quantity
    cart_item.total_price = cart_item.product.price * quantity
    db.commit()
    db.refresh(cart_item)
    return cart_item

def remove_cart_item(db: Session, cart_id: int):
    cart_item = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    db.delete(cart_item)
    db.commit()
    return {"detail": "Cart item removed successfully"}
