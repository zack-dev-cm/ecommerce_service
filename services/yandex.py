# services/yandex.py
import requests
from schemas import ProductCreate
import os


YANDEX_OAUTH_TOKEN = os.getenv("YANDEX_OAUTH_TOKEN")
YOUR_CAMPAIGN_ID = os.getenv("YOUR_CAMPAIGN_ID")

def create_yandex_product(product: ProductCreate):
    headers = {
        'Authorization': f'OAuth {YANDEX_OAUTH_TOKEN}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.partner.market.yandex.ru/v2/campaigns/{YOUR_CAMPAIGN_ID}/offer-mapping-entries.json'
    payload = {
        "offerMappingEntries": [
            {
                "offer": {
                    "shopSku": product.vendor_code,
                    "name": product.name,
                    "barcodes": [product.barcode],
                    "description": product.description,
                    "urls": ["https://example.com/product-page"],  # Update with actual URL
                    "pictures": [{"url": img} for img in product.images],
                    "vendor": product.brand,
                    "vendorCode": product.vendor_code,
                    "category": {"id": product.category_id}
                }
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response
