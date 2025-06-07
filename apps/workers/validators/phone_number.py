from datetime import date, time,datetime,timezone
from fastapi import HTTPException,status
from sqlalchemy import select
from apps.workers.models.workers import Reservation, Worker

def validate_phone(reservation_data):
    if not reservation_data.phone_number.isdigit() or not (900000000 <= int(reservation_data.phone_number) <= 999999999):
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Número de teléfono invalido"
            )  
