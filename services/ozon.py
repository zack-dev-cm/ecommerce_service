# services/ozon.py
import requests
from schemas import ProductCreate
import os

OZON_CLIENT_ID = os.getenv("YOUR_OZON_CLIENT_ID")
OZON_API_KEY = os.getenv("YOUR_OZON_API_KEY")

def create_ozon_product(product: ProductCreate):
    headers = {
        'Client-Id': OZON_CLIENT_ID,
        'Api-Key': OZON_API_KEY,
        'Content-Type': 'application/json'
    }
    url = 'https://api-seller.ozon.ru/v2/product/import'
    payload = {
        "items": [
            {
                "offer_id": product.vendor_code,
                "name": product.name,
                "barcode": product.barcode,
                "description": product.description,
                "category_id": product.category_id,
                "price": f"{product.price:.2f}",
                "vat": "0",
                "images": product.images,
                "attributes": [attr.dict() for attr in product.attributes]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response
