from config.db import get_db
from fastapi import Depends, HTTPException, status
from ..models.models import HairCut
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_all_haircuts( db: AsyncSession = Depends(get_db)  ):
    try:
        result = await db.execute(select(HairCut))
        haircuts = result.scalars()
        return haircuts
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )