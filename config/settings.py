from decouple import config, Csv
from pydantic_settings  import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # FASTAPI PROJECT
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Barbershop Project"
    
    # DATABASE (PostgreSQL Async)
    POSTGRES_USER: str = config("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", default="postgres")
    POSTGRES_SERVER: str = config("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: str = config("POSTGRES_PORT", default="5432")
    POSTGRES_DB: str = config("POSTGRES_DB", default="postgres")
    DATABASE_URL: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    # AUTHENTICATION
    SECRET_KEY: str = config("SECRET_KEY", default="YOUR-SECRET-KEY")

    # FRONTEND
    FRONTEND_URL: str = config("FRONTEND_URL", default="http://localhost:3000")

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = config(
        "BACKEND_CORS_ORIGINS",
        default="http://localhost,http://localhost:8000,http://localhost:3000",
        cast=Csv()
    )

    class Config:
        case_sensitive = True

settings = Settings()