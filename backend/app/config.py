from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@db:5432/velura_db"

    # JWT
    SECRET_KEY: str = "velura-super-secret-2024-chaimaa-backend"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Claude AI
    ANTHROPIC_API_KEY: Optional[str] = None

    # App
    APP_NAME: str = "Velura"
    BACKEND_PORT: int = 8000
    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


# Instance unique utilisée partout dans le projet
settings = Settings()