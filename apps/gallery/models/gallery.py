from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base(cls=AsyncAttrs)

class Gallery(Base):
    __tablename__ = "haircuts_gallery"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)  # Ruta de la imagen