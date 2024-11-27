# schemas.py
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class Attribute(BaseModel):
    id: int
    value: str

class ProductCreate(BaseModel):
    platform: str
    vendor_code: str
    name: str
    barcode: str
    description: str
    price: float
    brand: str
    category_id: int
    images: List[str]
    attributes: List[Attribute]
    supplier_id: Optional[int] = None  # Optional field

class ProductResponse(BaseModel):
    id: int
    platform: str
    vendor_code: str
    name: str
    barcode: str
    description: str
    price: float
    brand: str
    category_id: int
    images: List[str]
    attributes: List[Dict]
    supplier_id: Optional[int]

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    product_id: int
    quantity: int
    price: float
    region: str
    status: str

class OrderResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    order_date: datetime
    region: str
    status: str

    class Config:
        orm_mode = True

class SupplierCreate(BaseModel):
    name: str
    contact_info: str

class SupplierResponse(BaseModel):
    id: int
    name: str
    contact_info: str

    class Config:
        orm_mode = True


