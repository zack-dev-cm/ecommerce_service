# main.py
import json
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import uvicorn
import threading
from pyngrok import ngrok


from fastapi import APIRouter
from models import Product, Order, Supplier
from schemas import ProductCreate, ProductResponse, OrderCreate, OrderResponse, SupplierCreate, SupplierResponse
from database import engine, Base
from dependencies import get_db, verify_api_key
from services import wildberries, ozon, yandex, avito
from dashboards.dashboard import router as dashboard_router

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Management Service")

# Include dashboard routes
app.include_router(dashboard_router)

@app.post("/products/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(verify_api_key)
):
    # Save to database
    db_product = Product(
        platform=product.platform,
        vendor_code=product.vendor_code,
        name=product.name,
        barcode=product.barcode,
        description=product.description,
        price=product.price,
        brand=product.brand,
        category_id=product.category_id,
        images=json.dumps(product.images),
        attributes=json.dumps([attr.dict() for attr in product.attributes]),
        supplier_id=product.supplier_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    # Integrate with the respective platform
    platform = product.platform.lower()
    if platform == 'wildberries':
        response = wildberries.create_wildberries_product(product)
    elif platform == 'ozon':
        response = ozon.create_ozon_product(product)
    elif platform == 'yandex':
        response = yandex.create_yandex_product(product)
    elif platform == 'avito':
        response = avito.create_avito_product(product)
    else:
        raise HTTPException(status_code=400, detail="Unsupported platform")
    
    if response.status_code in [200, 201]:
        return ProductResponse(
            id=db_product.id,
            platform=db_product.platform,
            vendor_code=db_product.vendor_code,
            name=db_product.name,
            barcode=db_product.barcode,
            description=db_product.description,
            price=db_product.price,
            brand=db_product.brand,
            category_id=db_product.category_id,
            images=json.loads(db_product.images),
            attributes=json.loads(db_product.attributes),
            supplier_id=db_product.supplier_id
        )
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get("/dashboard/")
def get_dashboard(
    db: Session = Depends(get_db),
    api_key: str = Depends(verify_api_key)
):
    total_products = db.query(Product).count()
    return {"total_products": total_products}



# Orders Router
router_orders = APIRouter(
    prefix="/orders",
    tags=["Orders"],
    dependencies=[Depends(verify_api_key)],
    responses={404: {"description": "Not found"}},
)

@router_orders.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(
        product_id=order.product_id,
        quantity=order.quantity,
        price=order.price,
        region=order.region,
        status=order.status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router_orders.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

app.include_router(router_orders)

# Suppliers Router
router_suppliers = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"],
    dependencies=[Depends(verify_api_key)],
    responses={404: {"description": "Not found"}},
)

@router_suppliers.post("/", response_model=SupplierResponse)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = Supplier(
        name=supplier.name,
        contact_info=supplier.contact_info
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router_suppliers.get("/{supplier_id}", response_model=SupplierResponse)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

app.include_router(router_suppliers)


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Start ngrok and get the public URL
    public_url = ngrok.connect(8000)
    print(f"Public URL: {public_url}")
    
    # Run the FastAPI app in a separate thread
    thread = threading.Thread(target=run)
    thread.start()
