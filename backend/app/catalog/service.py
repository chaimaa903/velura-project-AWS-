import json                                        # ← LIGNE 1
from sqlalchemy.orm import Session
from typing import Optional
from app.catalog.models import Item
from app.catalog.schemas import ItemCreate


def get_all_items(
    db: Session,
    category: Optional[str] = None,
    size: Optional[str] = None,
    available: Optional[bool] = None
):
    query = db.query(Item)
    if category:
        query = query.filter(Item.category == category)
    if size:
        query = query.filter(Item.size == size)
    if available is not None:
        query = query.filter(Item.available == available)
    return query.all()                             # ← schemas gère la désérialisation


def get_item_by_id(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item and item.images and isinstance(item.images, str):
        try:
            item.images = json.loads(item.images)
        except:
            item.images = []
    return item


def search_items(
    db: Session,
    q: str,
    category: Optional[str] = None,
    size: Optional[str] = None,
    available: Optional[bool] = None
):
    query = db.query(Item).filter(
        Item.name.ilike(f"%{q}%") | Item.brand.ilike(f"%{q}%")
    )
    if category:
        query = query.filter(Item.category == category)
    if size:
        query = query.filter(Item.size == size)
    if available is not None:
        query = query.filter(Item.available == available)
    return query.all()


def create_item(db: Session, data: ItemCreate):
    item_data = data.model_dump()
    if item_data.get("images"):
        item_data["images"] = json.dumps(item_data["images"])
    item = Item(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    if item.images and isinstance(item.images, str):
        item.images = json.loads(item.images)
    return item