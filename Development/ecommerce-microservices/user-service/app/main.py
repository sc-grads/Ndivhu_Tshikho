
from fastapi import FastAPI
from database import engine
import model, router
from model import Base
import controller

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the router
app.include_router(router.router, prefix="/users")
