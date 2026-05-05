from sqlalchemy.orm import Session
from app.models.wardrobe_item import WardrobeItem
from app.schemas.wardrobe_item import WardrobeItemCreate, WardrobeItemUpdate

def create_wardrobe_item(db: Session, item: WardrobeItemCreate, user_id: int):
    db_item = WardrobeItem(**item.model_dump(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_user_wardrobe_items(db: Session, user_id: int):
    return db.query(WardrobeItem).filter(WardrobeItem.user_id == user_id).all()

def get_user_wardrobe_item_by_id(db: Session, item_id: int, user_id: int):
    return db.query(WardrobeItem).filter(WardrobeItem.id == item_id, WardrobeItem.user_id == user_id).first()

def update_wardrobe_item(db: Session, db_item: WardrobeItem, update_data: WardrobeItemUpdate):
    update_dict = update_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_wardrobe_item(db: Session, db_item: WardrobeItem):
    db.delete(db_item)
    db.commit()
    return True
