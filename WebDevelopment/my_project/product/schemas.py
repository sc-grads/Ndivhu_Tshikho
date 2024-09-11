from pydantic import BaseModel

class DispalySeller(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True
class Product(BaseModel):
    name:str
    description:str
    price:int

class  DisplayProduct(BaseModel):
    name: str
    description: str
    seller: DispalySeller
    class Config:
        orm_mode = True

class Seller(BaseModel):
    username: str
    email: str
    password: str



