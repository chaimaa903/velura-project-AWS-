from pydantic import BaseModel, field_validator
from typing import Optional, List
import json
# Ce que le frontend attend exactement (voir catalog/page.tsx)
class ItemOut(BaseModel):
    id: int
    name: str
    brand: str
    category: str
    size: str
    price: float
    images: Optional[List[str]] = None 
    available: bool
    
    @field_validator('images', mode='before')   # ← AJOUTER ce bloc
    @classmethod
    def parse_images(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except Exception:
                return []
        return v
    class Config:
        from_attributes = True

# Pour créer un item (admin)
class ItemCreate(BaseModel):
    name: str
    brand: str
    category: str
    size: str
    price: float
    images: Optional[List[str]] = None 