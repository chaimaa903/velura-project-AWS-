from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    """
    Table PostgreSQL : users
    
    Colonnes :
    - id           → clé primaire auto-incrémentée
    - name         → prénom + nom de l'utilisateur
    - email        → unique, utilisé pour login
    - password_hash→ mot de passe hashé bcrypt (jamais en clair)
    - created_at   → date de création automatique
    """
    __tablename__ = "users"

    id           = Column(Integer, primary_key=True, index=True)
    name         = Column(String(100), nullable=False)
    email        = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at   = Column(DateTime(timezone=True), server_default=func.now())