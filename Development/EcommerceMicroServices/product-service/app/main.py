from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import product_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router.router, prefix= "/api/products")
