from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WardrobeItemBase(BaseModel):
    image_url: str
    category: Optional[str] = None
    color: Optional[str] = None
    style: Optional[str] = None
    season: Optional[str] = None
    tags: Optional[str] = None

class WardrobeItemCreate(WardrobeItemBase):
    pass

class WardrobeItemResponse(WardrobeItemBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
