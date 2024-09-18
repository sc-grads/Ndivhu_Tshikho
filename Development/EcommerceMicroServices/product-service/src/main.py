from fastapi import FastAPI
from router import product_router
from database import Base, engine
from logging_config import setup_logging, logger  # Import logger and setup function

# Initialize the FastAPI app
app = FastAPI()

# Setup logging for this service
setup_logging(service_name="product-service")

# Log the service start
logger.info("Starting product-service")

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the product router
app.include_router(product_router.router)

