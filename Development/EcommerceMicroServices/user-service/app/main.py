from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import auth_router  # Assuming auth_router defines the user-related routes
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the auth_router with a prefix
app.include_router(auth_router.router)
