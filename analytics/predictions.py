# analytics/predictions.py
import pandas as pd
from sqlalchemy.orm import Session
from models import Order
from typing import Dict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def predict_sales(db: Session) -> Dict[str, any]:
    orders = db.query(Order).all()
    data = [{
        "product_id": order.product_id,
        "order_date": order.order_date,
        "quantity": order.quantity,
        "price": order.price
    } for order in orders]
    df = pd.DataFrame(data)
    df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
    df_grouped = df.groupby(['product_id', 'order_month']).agg({'quantity': 'sum'}).reset_index()

    # Pivot the data to have months as features
    pivot = df_grouped.pivot(index='product_id', columns='order_month', values='quantity').fillna(0)
    pivot = pivot.reset_index()

    # For simplicity, predict next month's sales based on previous months
    # This is a naive approach; in production, consider more sophisticated models
    features = pivot.columns[1:-1]
    target = pivot.columns[-1]

    X = pivot[features]
    y = pivot[target]

    if X.empty or y.empty:
        return {"prediction": "Not enough data to perform prediction."}

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    # Example prediction result
    result = {
        "predictions": predictions.tolist(),
        "mean_squared_error": mse
    }

    return {"sales_prediction": result}
