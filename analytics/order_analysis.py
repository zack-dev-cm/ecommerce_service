# analytics/order_analysis.py
from sqlalchemy.orm import Session
from models import Order
from typing import Dict

def order_analysis(db: Session) -> Dict[str, any]:
    orders = db.query(Order).all()
    data = [{
        "region": order.region,
        "status": order.status,
        "price": order.price
    } for order in orders]
    df = pd.DataFrame(data)
    summary = df.groupby(['region', 'status']).agg({'price': 'sum', 'status': 'count'}).reset_index()
    summary = summary.rename(columns={'price': 'total_revenue', 'status': 'order_count'})
    result = summary.to_dict(orient='records')
    return {"order_analysis": result}
