# users/profile.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserResponse
from models import User
from dependencies import get_db
from users.auth import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=UserResponse)
def read_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/", response_model=UserResponse)
def update_profile(updated_user: UserResponse, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.username = updated_user.username
    db.commit()
    db.refresh(user)
    return user
