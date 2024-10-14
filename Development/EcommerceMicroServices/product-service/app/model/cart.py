# src/models/cart.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CartItem(Base):
    __tablename__ = 'cart_item'
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, default=1)
    
    product = relationship("Product")  # Assuming you have a Product model
