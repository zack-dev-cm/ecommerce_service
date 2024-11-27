# dashboards/dashboard.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db, verify_api_key
from analytics import abc_analysis, xyz_analysis, specific_profit, order_analysis, predict_sales

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
    dependencies=[Depends(verify_api_key)],
    responses={404: {"description": "Not found"}},
)

@router.get("/abc")
def get_abc_analysis(db: Session = Depends(get_db)):
    return abc_analysis(db)

@router.get("/xyz")
def get_xyz_analysis(db: Session = Depends(get_db)):
    return xyz_analysis(db)

@router.get("/specific_profit")
def get_specific_profit(db: Session = Depends(get_db)):
    return specific_profit(db)

@router.get("/order_analysis")
def get_order_analysis(db: Session = Depends(get_db)):
    return order_analysis(db)

@router.get("/sales_prediction")
def get_sales_prediction(db: Session = Depends(get_db)):
    return predict_sales(db)
