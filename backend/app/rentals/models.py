from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func
from app.database import Base

class Rental(Base):
    __tablename__ = "rentals"

    id          = Column(Integer, primary_key=True, index=True)
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=False)
    item_id     = Column(Integer, ForeignKey("items.id"), nullable=False)
    rented_at   = Column(DateTime(timezone=True), server_default=func.now())
    returned_at = Column(DateTime(timezone=True), nullable=True)
    status      = Column(String, default="active")  # "active", "returned"
    item        = relationship("Item") 