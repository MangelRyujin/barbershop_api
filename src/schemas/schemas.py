from pydantic import BaseModel, Field
from datetime import date, time

class HairCutSchema(BaseModel):
    id: int
    name: str
    small_description: str
    price: float

    class Config:
        from_attributes = True  # Para compatibilidad con ORM (antes orm_mode)
        orm_mode = True

class GallerySchema(BaseModel):
    id: int
    name: str
    image: str

    class Config:
        from_attributes = True  # Para compatibilidad con ORM (antes orm_mode)
        orm_mode = True

class WorkerSchema(BaseModel):
    id: int
    image: str
    user_id: int | None = None

    class Config:
        from_attributes = True  # Para compatibilidad con ORM (antes orm_mode)
        orm_mode = True

class ReservationCreateSchema(BaseModel):
    worker_id: int
    name: str
    phone_number: str = Field(..., min_length=9, max_length=15)
    date: date
    time: time

class ReservationSchema(ReservationCreateSchema):
    id: int
    state: str

    class Config:
        from_attributes = True  # Para compatibilidad con ORM (antes orm_mode)
        orm_mode = True