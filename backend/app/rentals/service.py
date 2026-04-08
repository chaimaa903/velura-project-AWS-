from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.rentals.models import Rental
from app.catalog.models import Item
from app.rentals.schemas import RentalCreate, RentalOut
from sqlalchemy.orm import joinedload

def get_user_rentals(db: Session, user_id: int):
    rentals = (
        db.query(Rental)
        .filter(Rental.user_id == user_id)
        .options(joinedload(Rental.item))                      # ← 1 seule query
        .all()
    )
    return [
        RentalOut(
            id=r.id,
            itemName=r.item.name if r.item else "Unknown",
            rentedAt=r.rented_at.strftime("%Y-%m-%d"),
            status=r.status
        )
        for r in rentals
    ]

def create_rental(db: Session, user_id: int, data: RentalCreate):
    """Louer un item"""
    # Vérifier disponibilité
    item = db.query(Item).filter(Item.id == data.item_id).first()
    if not item or not item.available:
        return None

    try:
        rental = Rental(user_id=user_id, item_id=data.item_id, status="active")
        item.available = False
        db.add(rental)
        db.commit()
        db.refresh(rental)
        return rental
    except Exception:
        db.rollback()
        return None

def return_rental(db: Session, rental_id: int, user_id: int):
    """Retourner un item"""
    rental = db.query(Rental).filter(
        Rental.id == rental_id,
        Rental.user_id == user_id
    ).first()
    if not rental:
        return None

    rental.status = "returned"
    rental.returned_at = datetime.now(timezone.utc)

    # Remettre l'item disponible
    item = db.query(Item).filter(Item.id == rental.item_id).first()
    if item:
        item.available = True

    db.commit()
    db.refresh(rental)
    return rental