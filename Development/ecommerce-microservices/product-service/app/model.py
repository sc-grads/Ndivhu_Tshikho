
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    image_url = Column(String)  # URL to the uploaded image