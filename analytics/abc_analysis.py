# analytics/abc_analysis.py
import pandas as pd
from sqlalchemy.orm import Session
from models import Product, Order
from typing import Dict

def abc_analysis(db: Session) -> Dict[str, any]:
    # Retrieve all orders
    orders = db.query(Order).all()
    data = [{
        "product_id": order.product_id,
        "quantity": order.quantity,
        "price": order.price
    } for order in orders]
    df = pd.DataFrame(data)
    df['total'] = df['quantity'] * df['price']
    df_grouped = df.groupby('product_id').agg({'total': 'sum'}).reset_index()
    df_grouped = df_grouped.sort_values(by='total', ascending=False)
    total_revenue = df_grouped['total'].sum()
    df_grouped['cumulative'] = df_grouped['total'].cumsum()
    df_grouped['cumulative_percentage'] = 100 * df_grouped['cumulative'] / total_revenue

    # Define A, B, C categories
    def categorize(row):
        if row['cumulative_percentage'] <= 80:
            return 'A'
        elif row['cumulative_percentage'] <= 95:
            return 'B'
        else:
            return 'C'

    df_grouped['category'] = df_grouped.apply(categorize, axis=1)
    result = df_grouped.to_dict(orient='records')
    return {"abc_analysis": result}
