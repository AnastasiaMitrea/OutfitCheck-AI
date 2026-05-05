from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.wardrobe_item import WardrobeItemCreate, WardrobeItemUpdate, WardrobeItemResponse
from app.services import wardrobe_item as wardrobe_service
from app.routers.auth import get_current_user

router = APIRouter(prefix="/wardrobe", tags=["wardrobe"])

@router.post("/items", response_model=WardrobeItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: WardrobeItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return wardrobe_service.create_wardrobe_item(db=db, item=item, user_id=current_user.id)

@router.get("/items", response_model=List[WardrobeItemResponse])
def get_items(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return wardrobe_service.get_user_wardrobe_items(db=db, user_id=current_user.id)

@router.get("/items/{item_id}", response_model=WardrobeItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_item = wardrobe_service.get_user_wardrobe_item_by_id(db=db, item_id=item_id, user_id=current_user.id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Wardrobe item not found")
    return db_item

@router.put("/items/{item_id}", response_model=WardrobeItemResponse)
def update_item(item_id: int, item_update: WardrobeItemUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_item = wardrobe_service.get_user_wardrobe_item_by_id(db=db, item_id=item_id, user_id=current_user.id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Wardrobe item not found")
    return wardrobe_service.update_wardrobe_item(db=db, db_item=db_item, update_data=item_update)

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_item = wardrobe_service.get_user_wardrobe_item_by_id(db=db, item_id=item_id, user_id=current_user.id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Wardrobe item not found")
    wardrobe_service.delete_wardrobe_item(db=db, db_item=db_item)
