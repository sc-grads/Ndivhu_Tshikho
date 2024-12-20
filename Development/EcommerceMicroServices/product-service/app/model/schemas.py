# app/model/schemas.py
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image_url: str  # This can be added after processing the file

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True  # This allows returning SQLAlchemy models directly
