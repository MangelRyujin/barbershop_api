from fastapi import APIRouter,Depends
from typing import List
from apps.gallery.schemas.gallery import GallerySchema
from apps.gallery.services.gallery import get_all_gallery

router = APIRouter()

@router.get("/all-pictures", response_model=List[GallerySchema])
async def all_haircuts(gallery: GallerySchema = Depends(get_all_gallery))-> list:
    return gallery