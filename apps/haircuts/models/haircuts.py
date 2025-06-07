from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import  declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base(cls=AsyncAttrs)

class HairCut(Base):
    __tablename__ = "haircuts_haircut"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    small_description = Column(String(100), nullable=False)
    price = Column(Float, default=0)
