# app/model/cart.py
from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, default=1)
    total_price = Column(Float)

    product = relationship("Product", backref="cart_items")
