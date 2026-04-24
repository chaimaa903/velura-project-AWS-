from pydantic_settings import BaseSettings
from typing import Optional
import boto3
import json


def get_secrets_from_aws():
    """Récupère les secrets depuis AWS Secrets Manager"""
    try:
        client = boto3.client(
            'secretsmanager',
            region_name='eu-west-1'
        )
        secret = client.get_secret_value(SecretId="velura/production")
        return json.loads(secret['SecretString'])
    except Exception:
        # En local → utiliser les variables d'environnement normales
        return {}

# Charger les secrets AWS si on est en production
_secrets = get_secrets_from_aws()

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = _secrets.get(
        "DATABASE_URL",
        "postgresql://postgres:password@db:5432/velura_db"  # fallback local
    )

    # JWT
    SECRET_KEY: str = _secrets.get(
        "SECRET_KEY",
        "velura-super-secret-2024-chaimaa-backend"  # fallback local
    )
    ALGORITHM: str = _secrets.get("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(_secrets.get(
        "ACCESS_TOKEN_EXPIRE_MINUTES", 60
    ))

    # Claude AI
    ANTHROPIC_API_KEY: Optional[str] = _secrets.get(
        "ANTHROPIC_API_KEY",
        None
    )

    # App
    APP_NAME: str = "Velura"
    BACKEND_PORT: int = 8000
    FRONTEND_URL: str = _secrets.get(
        "FRONTEND_URL",
        "http://localhost:3000"
    )

    class Config:
        env_file = ".env"

settings = Settings()