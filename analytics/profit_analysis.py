# analytics/profit_analysis.py
from sqlalchemy.orm import Session
from models import Product, Order
from typing import Dict

def specific_profit(db: Session) -> Dict[str, any]:
    # Calculate profit per product
    orders = db.query(Order).all()
    data = [{
        "product_id": order.product_id,
        "quantity": order.quantity,
        "price": order.price
    } for order in orders]
    df = pd.DataFrame(data)
    df['total_revenue'] = df['quantity'] * df['price']
    # Assume fixed costs for simplicity; in reality, fetch from database or configurations
    fixed_costs = 1000  # Example value
    profit = df.groupby('product_id').agg({'total_revenue': 'sum'}).reset_index()
    profit['specific_profit'] = profit['total_revenue'] - fixed_costs
    result = profit.to_dict(orient='records')
    return {"specific_profit": result}
