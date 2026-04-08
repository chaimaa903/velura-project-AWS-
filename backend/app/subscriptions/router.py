from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.subscriptions import service, schemas
from app.auth.service import get_current_user
from app.users.models import User

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])

# GET /api/subscriptions/me
# → dashboard affiche le plan actuel de l'user
@router.get("/me", response_model=schemas.SubscriptionOut)
def get_my_subscription(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    sub = service.get_user_subscription(db, current_user.id)
    if not sub:
        raise HTTPException(status_code=404, detail="Aucun abonnement actif")
    return sub

# POST /api/subscriptions
# → user clique "Subscribe" sur Essential / Signature / Couture
@router.post("", response_model=schemas.SubscriptionOut, status_code=201)
def subscribe(
    data: schemas.SubscriptionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return service.create_subscription(db, current_user.id, data)

# PUT /api/subscriptions/upgrade
# → user change de plan (ex: Essential → Couture)
@router.put("/upgrade", response_model=schemas.SubscriptionOut)
def upgrade(
    data: schemas.SubscriptionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return service.upgrade_subscription(db, current_user.id, data)

# DELETE /api/subscriptions/me
# → user annule son abonnement
@router.delete("/me", response_model=schemas.SubscriptionOut)
def cancel(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    sub = service.cancel_subscription(db, current_user.id)
    if not sub:
        raise HTTPException(status_code=404, detail="Aucun abonnement à annuler")
    return sub