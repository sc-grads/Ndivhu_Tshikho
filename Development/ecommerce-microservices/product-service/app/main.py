from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import model
from database import engine
import router
from model import Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
# Mount the images directory
app.mount("/images", StaticFiles(directory="images"), name="images")

# Include the router
app.include_router(router.router, prefix="/products")

