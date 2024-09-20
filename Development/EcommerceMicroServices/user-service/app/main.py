from fastapi import FastAPI
from router import auth_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.router)
