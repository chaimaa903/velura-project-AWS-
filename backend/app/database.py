from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Moteur de connexion à PostgreSQL
engine = create_engine(settings.DATABASE_URL)

# Factory de sessions DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe de base pour tous les models SQLAlchemy
Base = declarative_base()


def get_db():
    """
    Dependency FastAPI — injectée dans chaque router.
    Ouvre une session DB, la fournit, puis la ferme automatiquement.
    
    Utilisation dans un router :
        db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()