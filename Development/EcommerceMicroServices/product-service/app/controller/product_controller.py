
from sqlalchemy.orm import Session
from model.product import Product

from sqlalchemy.orm import Session
from model.product import Product
import shutil
import os

# Directory where uploaded images will be stored
UPLOAD_DIRECTORY = "path/to/upload/directory"  # Change to your desired upload directory

def create_product(db: Session, name: str, description: str, price: float, file: UploadFile):
    # Ensure the upload directory exists
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
    
    # Save the uploaded file
    image_url = f"{UPLOAD_DIRECTORY}/{file.filename}"
    with open(image_url, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Create the product
    db_product = Product(name=name, description=description, price=price, image_url=image_url)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()