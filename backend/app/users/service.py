from sqlalchemy.orm import Session
from app.users.models import User
from app.users.schemas import UserCreate, UserUpdate
from app.auth.service import hash_password          # ← hash via auth/service.py
from fastapi import HTTPException


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return user


def create_user(db: Session, user: UserCreate):
    hashed = hash_password(user.password)           # ← utilise hash_password importé
    db_user = User(name=user.name, email=user.email, password_hash=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, data: UserUpdate):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    if data.name:
        user.name = data.name
    if data.email:
        user.email = data.email
    db.commit()
    db.refresh(user)
    return user