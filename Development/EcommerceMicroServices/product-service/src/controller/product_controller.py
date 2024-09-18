from models.product import Product
from sqlalchemy.orm import Session

def create_product(db: Session, name: str, description: str, price: float):
    db_product = Product(name=name, description=description, price=price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(Product).all()

def update_product(db: Session, product_id: int, name: str, description: str, price: float):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        product.name = name
        product.description = description
        product.price = price
        db.commit()
        db.refresh(product)
        return product
    return None

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False
