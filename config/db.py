from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from config.settings import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False, # Change False in production
    pool_size=40,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=3600,
    pool_pre_ping=True,     # Verificar conexiones antes de usarlas
    connect_args={
        "server_settings": {
            "timezone": "utc",
            "application_name": settings.PROJECT_NAME  
        },
        "command_timeout": 60,  
    },
    hide_parameters=False, # Change True in production
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session