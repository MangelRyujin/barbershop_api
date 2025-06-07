from config.db import get_db
from fastapi import Depends, HTTPException,status
from apps.haircuts.models.haircuts import HairCut
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_all_haircuts( db: AsyncSession = Depends(get_db)  ):
    try:
        result = await db.execute(select(HairCut))
        haircuts = result.scalars()
        return haircuts
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )