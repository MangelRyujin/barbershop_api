from fastapi import HTTPException,status
from sqlalchemy import select
from apps.workers.models.workers import  Worker
from apps.workers.schemas.reservation import ReservationCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession

async def validate_worker_exists(reservation_data:ReservationCreateSchema,db:AsyncSession):
    worker = await db.execute(
            select(Worker).where(Worker.id == reservation_data.worker_id))
    if not worker.scalar_one_or_none():
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Trabajador no encontrado"
            )