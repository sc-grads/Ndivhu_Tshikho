import datetime
from datetime import date, time, timedelta
from typing import Set, List
from uuid import UUID

from fastapi import FastAPI, Form
from pydantic import BaseModel, Field, HttpUrl

class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime.datetime  # Use datetime.datetime for both date and time
    end_time: datetime.datetime  # Same here
    repeat_time: time  # Use datetime.time for time only
    execute_after: timedelta  # Use datetime.timedelta for durations

class Profile(BaseModel):
    name: str
    email: str
    age: int

class Image(BaseModel):
    url: str
    name: str

class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the item")
    discount: int
    discounted_price: float
    tags: Set[str] = []
    image: List[Image]

    class Config:
        schema_extra = {
            "example": {
                "name": "Phone",
                "price": 0,
                "discount": 0,
                "discounted_price": 0,
                "tags": ["Electronics", "Computers"],
                "image": [
                    {"url": "http://www.google.com", "name": "phone image"},
                    {"url": "http://www.google.com", "name": "phone view"}
                ]
            }
        }

class Offer(BaseModel):
    name: str
    description: str
    price: float = Field(title="Price of the offer")
    products: List[Product]

class User(BaseModel):
    name: HttpUrl
    email: str


app = FastAPI()

@app.post('/login')
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

@app.post('/addevent')
def addevent(event: Event):
    return event

@app.post('/addoffer')
def addoffer(offer: Offer):
    return offer

@app.post('/purchase')
def purchase(user: User, product: Product):
    return {'user': user, 'product': product}

@app.post("/addproduct/{product_id}")
def add_product(product: Product, product_id: int):
    product.discounted_price = product.price - (product.price * product.discount) / 100
    return {"product_id": product_id, "product": product}

# Commented out section for user
# @app.post('/adduser')
# def adduser(profile: Profile):
#     return {'user data'}

@app.get("/user/admin")
def admin():
    return {"This is an admin page"}

@app.get("/user/{username}")
def profile(username: str):
    return {f'This is a profile page for {username}'}

@app.get("/products")
def products(id: int = 1, price: int = 0):
    return {f"Product with id: {id} and price {price}"}
