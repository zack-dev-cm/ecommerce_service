# analytics/xyz_analysis.py
import pandas as pd
from sqlalchemy.orm import Session
from models import Product, Order
from typing import Dict

def xyz_analysis(db: Session) -> Dict[str, any]:
    # Calculate sales frequency and variability
    orders = db.query(Order).all()
    data = [{
        "product_id": order.product_id,
        "order_date": order.order_date
    } for order in orders]
    df = pd.DataFrame(data)
    df['order_month'] = df['order_date'].dt.to_period('M')
    sales_frequency = df.groupby('product_id').agg({'order_month': 'nunique'}).reset_index()
    sales_variability = df.groupby('product_id').agg({'order_date': 'std'}).reset_index()
    sales_variability['order_date'] = sales_variability['order_date'].fillna(0)

    # Merge frequency and variability
    analysis = pd.merge(sales_frequency, sales_variability, on='product_id')
    analysis = analysis.rename(columns={'order_month': 'frequency', 'order_date': 'variability'})
    analysis['variability'] = analysis['variability'].astype(float)
    analysis['frequency'] = analysis['frequency'].astype(int)

    # Define X, Y, Z categories
    def categorize(row):
        if row['frequency'] > 12:
            if row['variability'] < 10:
                return 'X'
            elif row['variability'] < 20:
                return 'Y'
            else:
                return 'Z'
        else:
            if row['variability'] < 10:
                return 'Y'
            else:
                return 'Z'

    analysis['category'] = analysis.apply(categorize, axis=1)
    result = analysis.to_dict(orient='records')
    return {"xyz_analysis": result}
