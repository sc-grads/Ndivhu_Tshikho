from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Response
from .routers import product, seller
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal,get_db
from passlib.context import CryptContext

app = FastAPI()
title = "Product API"
description = "This is a simple CRUD API for products"
term_of_service = {"url": "https://www.google.com",
                   "contact": "https://www.google.com"}


app.include_router(product.router)
app.include_router(seller.router)


models.Base.metadata.create_all(bind=engine)
