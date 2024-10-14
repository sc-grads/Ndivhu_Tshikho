from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image: str  # Include image URL or filename

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: str  # Include image in the response

    class Config:
        orm_mode = True
