from fastapi import FastAPI
from router import product_router
from database import Base, engine
import logging
from logging_config import setup_logging

app = FastAPI()

# Setup logging
setup_logging(service_name="product-service")

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the product router
app.include_router(product_router.router)
