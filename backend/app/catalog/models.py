from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String, nullable=False)
    brand    = Column(String, nullable=False)
    category = Column(String, nullable=False)   # "dress", "blazer", etc.
    size     = Column(String, nullable=False)   # "S", "M", "L"
    price    = Column(Float, nullable=False)    # prix en MAD
    images   = Column(Text, nullable=True)    # URL image S3
    available = Column(Boolean, default=True)   # disponible à la location