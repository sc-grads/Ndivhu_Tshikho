from fastapi import FastAPI
from routers import auth_router, product_router
from database import Base, engine
import logging
from logging_config import *
from fastapi.staticfiles import StaticFiles
from opentelemetry_config import init_tracing  # Import OpenTelemetry configuration


# Initialize the FastAPI app
app = FastAPI()

# Initialize OpenTelemetry tracing
init_tracing(app)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the authentication and product routers
app.include_router(auth_router.router)
app.include_router(product_router.router)

# Set up logging
logger = logging.getLogger(__name__)
logger.info("Application startup: FastAPI e-commerce backend")
