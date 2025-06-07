from config.db import get_db
from fastapi import Depends, HTTPException,status
from apps.gallery.models.gallery import Gallery
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_all_gallery( db: AsyncSession = Depends(get_db)  ):
    try:
        result = await db.execute(select(Gallery))
        gallery = result.scalars()
        return gallery
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )