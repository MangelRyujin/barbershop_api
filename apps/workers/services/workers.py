from config.db import get_db
from fastapi import Depends, HTTPException,status
from apps.workers.models.workers import Worker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_all_workers( db: AsyncSession = Depends(get_db)  ):
    try:
        result = await db.execute(select(Worker))
        workers = result.scalars()
        return workers
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )