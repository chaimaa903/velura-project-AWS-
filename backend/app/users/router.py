from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.users import service, schemas
from app.auth.service import get_current_user
from app.users.models import User

router = APIRouter(prefix="/users", tags=["users"])

# GET /api/users/me → frontend dashboard l'utilise
@router.get("/me", response_model=schemas.UserOut)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user

# PUT /api/users/me → modifier son profil
@router.put("/me", response_model=schemas.UserOut)
def update_my_profile(
    data: schemas.UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    updated = service.update_user(db, current_user.id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated