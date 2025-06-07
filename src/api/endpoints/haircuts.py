from fastapi import APIRouter, HTTPException,Depends,status
from typing import List
from ...schemas.schemas import HairCutSchema
from ...services.haircuts import get_all_haircuts
from ...models.models import  HairCut # Assuming you have a way to import your models
from config.db import get_db  # Assuming you have a database session setup
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/haircuts", response_model=List[HairCutSchema])
async def all_haircuts(haircuts: HairCutSchema = Depends(get_all_haircuts))-> list:
    return haircuts