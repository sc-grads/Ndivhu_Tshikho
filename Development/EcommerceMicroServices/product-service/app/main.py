from fastapi import FastAPI
from router import product_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_router.router, prefix="/products")
