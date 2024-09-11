from fastapi import APIRouter, Depends, HTTPException
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Response

from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import engine, SessionLocal,get_db
from passlib.context import CryptContext

router = APIRouter(
    tags=['Product'],
    prefix="/product"
)


@router.get('/')
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.put('//{id}')
def update(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {'Product successfully updated'}

@router.delete('/{id}')
def delete_product(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete()
    db.commit()
    return {'Product deleted'}

@router.get('/{id}', response_model=List[schemas.DisplayProduct])
def get_product(id: int, db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.id == id).all()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Product not found')
    return products


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name,
        description=request.description,
        price=request.price,
        seller_id=1
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
