from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from app.database import get_db
from app.catalog import service, schemas
from app.auth.service import get_current_user
from app.users.models import User

router = APIRouter(prefix="/catalog", tags=["catalog"])

# GET /api/catalog/items
# → appelé par getItems() dans api.ts → catalog/page.tsx
@router.get("/items", response_model=List[schemas.ItemOut])
def get_items(
    category: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    available: Optional[bool] = Query(None),
    q: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    if q:
        return service.search_items(db, q)
    return service.get_all_items(db, category, size, available)

# GET /api/catalog/items/{id}
# → catalog/[id]/page.tsx
@router.get("/items/{item_id}", response_model=schemas.ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = service.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return item

# POST /api/catalog/items (admin seulement)
@router.post("/items", response_model=schemas.ItemOut, status_code=201)
def create_item(
    data: schemas.ItemCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return service.create_item(db, data)