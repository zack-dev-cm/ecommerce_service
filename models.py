# models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, index=True)
    vendor_code = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    barcode = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Float)
    brand = Column(String)
    category_id = Column(Integer)
    images = Column(String)  # JSON string
    attributes = Column(String)  # JSON string

    orders = relationship("Order", back_populates="product")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)
    order_date = Column(DateTime, default=datetime.utcnow)
    region = Column(String)
    status = Column(String)  # e.g., delivered, in transit, returned

    product = relationship("Product", back_populates="orders")

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    contact_info = Column(String)
    products = relationship("Product", back_populates="supplier")

Product.supplier = relationship("Supplier", back_populates="products")
