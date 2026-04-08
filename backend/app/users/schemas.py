from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):      # ← register onnées reçues à l'inscription
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):         # ← retourné au frontend Données renvoyées (jamais le mot de passe !)
    id: int
    name: str
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):      # ← modifier profil 
    """
    Ce que le frontend ENVOIE pour modifier le profil.
    Utilisé par : PUT /api/users/me → dashboard/page.tsx
    Tous les champs sont optionnels (on modifie ce qu'on veut)
    """
    name: Optional[str] = None
    email: Optional[EmailStr] = None