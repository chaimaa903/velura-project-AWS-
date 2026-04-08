from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Ce que getRentals() dans api.ts attend exactement
class RentalOut(BaseModel):
    id: int
    itemName: str       # nom de l'item loué
    rentedAt: str       # date formatée
    status: str         # "active" ou "returned"


# Pour créer une location
class RentalCreate(BaseModel):
    item_id: int

class RentalCreateOut(BaseModel):          # ← AJOUTER ce bloc entier
    message: str
    rental_id: int    