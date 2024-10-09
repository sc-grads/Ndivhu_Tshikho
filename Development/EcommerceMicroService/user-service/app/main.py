from importlib import metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from database import DATABASE_URL, database
from controller.auth_controller import router as auth_router

app = FastAPI()

# Add CORS middleware to allow communication between services
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific frontend URL in production (e.g., ["http://localhost:8000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    # Create the tables in the database
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)

app.include_router(auth_router, prefix="/api/users")
