from fastapi import FastAPI
from routers import auth_router
from database import Base, engine

# Initialize the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the authentication router
app.include_router(auth_router.router)
