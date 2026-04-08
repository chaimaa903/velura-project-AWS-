from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.rentals import service, schemas
from app.auth.service import get_current_user
from app.users.models import User

router = APIRouter(prefix="/rentals", tags=["rentals"])

# GET /api/rentals
# → appelé par getRentals() dans api.ts → dashboard/rentals/page.tsx
@router.get("", response_model=List[schemas.RentalOut])
def get_my_rentals(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return service.get_user_rentals(db, current_user.id)

# POST /api/rentals
# → louer un item depuis catalog/[id]/page.tsx
@router.post("", response_model=schemas.RentalCreateOut, status_code=201)
def rent_item(
    data: schemas.RentalCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    rental = service.create_rental(db, current_user.id, data)
    if not rental:
        raise HTTPException(status_code=400, detail="Item non disponible")
    return {"message": "Location créée avec succès", "rental_id": rental.id}

# PUT /api/rentals/{rental_id}/return
# → retourner un item
@router.put("/{rental_id}/return")
def return_item(
    rental_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    rental = service.return_rental(db, rental_id, current_user.id)
    if not rental:
        raise HTTPException(status_code=404, detail="Location non trouvée")
    return {"message": "Item retourné avec succès"}