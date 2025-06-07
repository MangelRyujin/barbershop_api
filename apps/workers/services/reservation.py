from apps.workers.validators.datetime import validate_reservation_exists, validate_future_date
from apps.workers.validators.phone_number import validate_phone
from apps.workers.validators.worker import validate_worker_exists
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from apps.workers.models.workers import Reservation
from apps.workers.schemas.reservation import ReservationCreateSchema, ReservationSchema

async def create_reservation(
    reservation_data: ReservationCreateSchema, 
    db: AsyncSession
) -> ReservationSchema:
    try:
        validate_phone(reservation_data)
            
        await validate_worker_exists(reservation_data,db)
            
        validate_future_date(reservation_data)
       
        await validate_reservation_exists(reservation_data,db)
             
        new_reservation = Reservation(
            worker_id=reservation_data.worker_id,
            name=reservation_data.name,
            phone_number=reservation_data.phone_number,
            reservation_date=reservation_data.reservation_date,
            reservation_time=reservation_data.reservation_time,
            state="1"
        )
        
        db.add(new_reservation)
        await db.commit()
        await db.refresh(new_reservation)
        
        return ReservationSchema.model_validate(new_reservation)
        
    except HTTPException:
        raise  
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"detail: {str(e)}"
        )