# users/favorites.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import ProductResponse
from models import Favorite, Product
from dependencies import get_db
from users.auth import get_current_user
from typing import List

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"],
    responses={404: {"description": "Not found"}},
)

@router.post("/{product_id}", response_model=ProductResponse)
def add_favorite(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    favorite = db.query(Favorite).filter(Favorite.user_id == current_user.id, Favorite.product_id == product_id).first()
    if favorite:
        raise HTTPException(status_code=400, detail="Product already in favorites")
    new_favorite = Favorite(user_id=current_user.id, product_id=product_id)
    db.add(new_favorite)
    db.commit()
    return product

@router.get("/", response_model=List[ProductResponse])
def get_favorites(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    favorites = db.query(Favorite).filter(Favorite.user_id == current_user.id).all()
    products = [fav.product for fav in favorites]
    return products

@router.delete("/{product_id}", response_model=dict)
def remove_favorite(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    favorite = db.query(Favorite).filter(Favorite.user_id == current_user.id, Favorite.product_id == product_id).first()
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    db.delete(favorite)
    db.commit()
    return {"detail": "Favorite removed successfully"}
