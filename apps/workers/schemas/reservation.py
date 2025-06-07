from typing import Optional
from pydantic import BaseModel, Field, validator
from datetime import date,datetime, time, timezone  


class ReservationCreateSchema(BaseModel):
    worker_id: int
    name: str
    phone_number: str = Field(..., min_length=9, max_length=9)
    reservation_date: date
    reservation_time: time
    state: Optional[str] = "1"

    # @validator('phone_number')
    # def validate_phone(cls, v):
    #     if not v.isdigit() or not (900000000 <= int(v) <= 999999999):
    #         raise ValueError("Número de teléfono invalido")
    #     return v
    
    # @validator('reservation_date')
    # def validate_date_not_past(cls, v):
    #     if v < datetime.now().date():
    #         raise ValueError("La fecha no puede ser anterior al día actual")
    #     return v
    
    
    # @validator('reservation_time')
    # def validate_time_not_past(cls, v: time, values: dict):
    #     if 'date' in values:
    #         current_datetime = datetime.now(timezone.utc)  # Hora UTC con zona horaria
    #         v_aware = v.replace(tzinfo=timezone.utc)  # Convierte el tiempo a aware
            
    #         if values['date'] == current_datetime.date() and v_aware < current_datetime.time():
    #             raise ValueError("La hora no puede ser anterior a la hora actual")
    #     return v
    
    
class ReservationSchema(ReservationCreateSchema):
    id: int
    

    class Config:
        from_attributes = True
        orm_mode = True