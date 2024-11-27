# services/wildberries.py
import requests
from schemas import ProductCreate
from dotenv import load_dotenv
import os
import json

load_dotenv()

WILDBERRIES_API_TOKEN = os.getenv("WILDBERRIES_API_TOKEN")

def create_wildberries_product(product: ProductCreate):
    headers = {
        'Authorization': WILDBERRIES_API_TOKEN,
        'Content-Type': 'application/json'
    }
    url = 'https://content-api.wildberries.ru/api/v1/cards/upload'
    payload = {
        "vendorCode": product.vendor_code,
        "characteristics": [
            {
                "Country of origin": "China",
                "Name": product.name,
                "Brand": product.brand,
                "Description": product.description,
                "Images": [{"link": img} for img in product.images]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response
