from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Response

from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/product')
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.put('/product/{id}')
def update(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {'Product successfully updated'}

@app.delete('/product/{id}')
def delete_product(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete()
    db.commit()
    return {'Product deleted'}

@app.get('/product/{id}', response_model=List[schemas.DisplayProduct])
def get_product(id,response: Response, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail ='Product not found')
    return product


@app.post("/product", status_code=status.HTTP_201_CREATED)
def add_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name,
        description=request.description,
        price=request.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
