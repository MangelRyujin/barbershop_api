from fastapi import APIRouter,Depends
from typing import List
from apps.haircuts.schemas.haircuts import HairCutSchema
from apps.haircuts.services.haircuts import get_all_haircuts

router = APIRouter()

@router.get("/all-haircuts", response_model=List[HairCutSchema])
async def all_haircuts(haircuts: HairCutSchema = Depends(get_all_haircuts))-> list:
    return haircuts