from fastapi import FastAPI
from routers import auth_router
from database import Base, engine
import logging
from logging_config import *
from fastapi.staticfiles import StaticFiles

# Initialize the FastAPI app
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the authentication router
app.include_router(auth_router.router)
