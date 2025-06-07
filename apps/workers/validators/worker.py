from fastapi import HTTPException,status
from sqlalchemy import select
from apps.workers.models.workers import  CustomUser
from apps.workers.schemas.reservation import ReservationCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession

async def validate_worker_exists(reservation_data:ReservationCreateSchema,db:AsyncSession):
    worker = await db.execute(
            select(CustomUser).where(CustomUser.id == reservation_data.worker_id, CustomUser.is_worker == True))
    if not worker.scalar_one_or_none():
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Trabajador no encontrado"
            )