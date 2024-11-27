# services/avito.py
import requests
from schemas import ProductCreate
import os

AVITO_CLIENT_ID = os.getenv("AVITO_CLIENT_ID")
AVITO_CLIENT_SECRET = os.getenv("AVITO_CLIENT_SECRET")

def create_avito_product(product: ProductCreate):
    # Obtain access token
    token_url = 'https://api.avito.ru/token/'
    token_data = {
        'client_id': AVITO_CLIENT_ID,
        'client_secret': AVITO_CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    token_response = requests.post(token_url, data=token_data)
    access_token = token_response.json().get('access_token')
    if not access_token:
        raise Exception("Failed to obtain Avito access token")

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = 'https://api.avito.ru/core/v1/items'
    payload = {
        "category_id": product.category_id,  # Replace with actual category ID
        "title": product.name,
        "description": product.description,
        "price": int(product.price),
        "images": [{"url": img} for img in product.images],
        "params": [attr.dict() for attr in product.attributes]  
    }
    response = requests.post(url, headers=headers, json=payload)
    return response
