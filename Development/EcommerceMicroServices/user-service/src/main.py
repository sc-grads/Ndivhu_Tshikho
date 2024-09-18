from fastapi import FastAPI
from router import auth_router
from database import Base, engine
import logging
from logging_config import setup_logging

app = FastAPI()

# Setup logging
setup_logging(service_name="user-service")

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the user authentication router
app.include_router(auth_router.router)
