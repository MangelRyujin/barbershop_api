from sqlalchemy import Column, Integer, String,  ForeignKey, Date, Time, CheckConstraint
from sqlalchemy.orm import relationship, declarative_base, validates
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base(cls=AsyncAttrs)

class Worker(Base):
    __tablename__ = "workers_worker"
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=True)  


class Reservation(Base):
    __tablename__ = "workers_reservation"
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers_worker.id"))
    name = Column(String(255), nullable=False)
    phone_number = Column(String(15), nullable=False)
    reservation_date = Column(Date, nullable=False)
    reservation_time = Column(Time, nullable=False)
    state = Column(String(1), default="1")
    worker = relationship("Worker")
    
    