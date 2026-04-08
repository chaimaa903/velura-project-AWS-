from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    """
    Ce que le frontend envoie pour se connecter.
    Fichier frontend : app/auth/login/page.tsx
    Route           : POST /api/auth/login
    """
    email: EmailStr
    password: str

# Ce que le backend renvoie après login
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"