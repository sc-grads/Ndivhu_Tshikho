# src/controllers/product_controller.py

from sqlalchemy.orm import Session
from models.product import Product

def create_product(db: Session, name: str, description: str, price: float, image_url: str):
    db_product = Product(name=name, description=description, price=price, image_url=image_url)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, name: str, description: str, price: float, image_url: str):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db_product.name = name
        db_product.description = description
        db_product.price = price
        db_product.image_url = image_url
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
