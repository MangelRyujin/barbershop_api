from datetime import date, time,datetime
from fastapi import HTTPException,status
from sqlalchemy import select
from apps.workers.models.workers import Reservation,CustomUser
from sqlalchemy.ext.asyncio import AsyncSession

from apps.workers.schemas.reservation import ReservationCreateSchema


def validate_future_date(reservation_data:ReservationCreateSchema):
    current_datetime = datetime.now()
    reservation_datetime = datetime.combine(
            reservation_data.reservation_date,
            reservation_data.reservation_time
        )
    if reservation_datetime < current_datetime:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La fecha y hora de reservación no pueden ser en el pasado"
            )


async def validate_reservation_exists(reservation_data:ReservationCreateSchema,db:AsyncSession):
    existing_reservation = await db.execute(
            select(Reservation).where(
                Reservation.worker_id == reservation_data.worker_id,
                CustomUser.is_worker == True,
                CustomUser.id == reservation_data.worker_id,
                Reservation.reservation_date == reservation_data.reservation_date,
                Reservation.reservation_time == reservation_data.reservation_time
            )
        )
    if existing_reservation.scalar_one_or_none():
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una reservación para este trabajador en la misma fecha y hora"
            )