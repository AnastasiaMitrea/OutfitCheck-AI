from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class WardrobeItem(Base):
    __tablename__ = "wardrobe_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Core attributes
    image_url = Column(String, nullable=False)
    
    # Metadata extracted by AI Analyzer
    category = Column(String, nullable=True)  # e.g., "top", "bottom", "shoes"
    color = Column(String, nullable=True)     # e.g., "black", "navy"
    style = Column(String, nullable=True)     # e.g., "casual", "formal"
    season = Column(String, nullable=True)    # e.g., "summer", "winter"
    tags = Column(String, nullable=True)      # Comma-separated or JSON string
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # In a full implementation, you'd add:
    # user = relationship("User", back_populates="wardrobe_items")
