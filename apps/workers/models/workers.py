from sqlalchemy import Column, Integer, String,  ForeignKey, Date, Time,Boolean, CheckConstraint
from sqlalchemy.orm import relationship, declarative_base, validates
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base(cls=AsyncAttrs)


class CustomUser(Base):
    __tablename__ = "accounts_customuser"
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String(255), nullable=False)
    is_worker = Column(Boolean, nullable=True)  
    is_active = Column(Boolean, nullable=True) 
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)

class Reservation(Base):
    __tablename__ = "workers_reservation"
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("accounts_customuser.id"))
    name = Column(String(255), nullable=False)
    phone_number = Column(String(15), nullable=False)
    reservation_date = Column(Date, nullable=False)
    reservation_time = Column(Time, nullable=False)
    state = Column(String(1), default="1")
    worker = relationship("CustomUser")
    
    