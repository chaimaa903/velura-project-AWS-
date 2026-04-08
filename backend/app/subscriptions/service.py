from sqlalchemy.orm import Session
from app.subscriptions.models import Subscription
from app.subscriptions.schemas import SubscriptionCreate

def get_user_subscription(db: Session, user_id: int):
    """Retourne l'abonnement actif de l'user"""
    return db.query(Subscription).filter(
        Subscription.user_id == user_id,
        Subscription.status == "active"
    ).first()

def create_subscription(db: Session, user_id: int, data: SubscriptionCreate):
    """Souscrit à un plan — annule l'ancien si existant"""
    # Annuler l'abonnement actif existant
    existing = get_user_subscription(db, user_id)
    if existing:
        existing.status = "cancelled"
        

    sub = Subscription(
        user_id=user_id,
        plan=data.plan.value,   # "Essential", "Signature", "Couture"
        status="active"
    )
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub

def cancel_subscription(db: Session, user_id: int):
    """Annule l'abonnement actif"""
    sub = get_user_subscription(db, user_id)
    if sub:
        sub.status = "cancelled"
        db.commit()
        db.refresh(sub)
    return sub

def upgrade_subscription(db: Session, user_id: int, data: SubscriptionCreate):
    """Change de plan — même logique que create"""
    return create_subscription(db, user_id, data)