from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import schemas, service
from app.users import service as user_service
from app.users.schemas import UserCreate, UserOut

router = APIRouter(prefix="/auth", tags=["auth"])

# POST /api/auth/register ← page register du frontend
@router.post("/register", response_model=UserOut, status_code=201)
def register(data: UserCreate, db: Session = Depends(get_db)):
    existing = user_service.get_user_by_email(db, data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    return user_service.create_user(db, data)

# POST /api/auth/login ← page login du frontend
@router.post("/login", response_model=schemas.Token)
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = service.authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")
    token = service.create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}