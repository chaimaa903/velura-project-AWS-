from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

# Les 3 plans exacts du frontend
class PlanName(str, Enum):
    essential = "Essential"
    signature = "Signature"
    couture = "Couture"

# Ce que le frontend envoie quand l'user clique "Subscribe"
class SubscriptionCreate(BaseModel):
    plan: PlanName

# Ce que le backend renvoie
class SubscriptionOut(BaseModel):
    id: int
    user_id: int
    plan: str
    status: str
    start_date: datetime
    end_date: Optional[datetime] = None

    class Config:
        from_attributes = True