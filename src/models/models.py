from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base(cls=AsyncAttrs)

class HairCut(Base):
    __tablename__ = "haircuts_haircut"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    small_description = Column(String(100), nullable=False)
    price = Column(Float, default=0)

class Gallery(Base):
    __tablename__ = "haircuts_gallery"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)  # Ruta de la imagen

class Worker(Base):
    __tablename__ = "workers_worker"
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=True)  # Puedes relacionar con tabla de usuarios si la tienes

class Reservation(Base):
    __tablename__ = "workers_reservation"
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers_worker.id"))
    name = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    state = Column(String(1), default="1")
    worker = relationship("Worker")