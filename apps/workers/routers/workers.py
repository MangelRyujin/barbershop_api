from fastapi import APIRouter,Depends
from typing import List
from apps.workers.schemas.workers import CustomUserSchema
from apps.workers.schemas.reservation import ReservationCreateSchema, ReservationSchema
from apps.workers.services.workers import get_all_workers
from apps.workers.services.reservation import create_reservation
from config.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/all-workers", response_model=List[CustomUserSchema])
async def all_workers(workers: CustomUserSchema = Depends(get_all_workers))-> list:
    return workers

@router.post("/create-reservation", response_model=ReservationSchema)
async def create_reservation_endpoint(
    reservation_data: ReservationCreateSchema,
    db: AsyncSession = Depends(get_db)
):  
    return await create_reservation(reservation_data, db)
