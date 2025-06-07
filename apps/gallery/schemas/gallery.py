from typing import Optional
from pydantic import BaseModel, validator
from config.settings import settings

class GallerySchema(BaseModel):
    id: int
    name: str
    image: str
    image_url: Optional[str] = None 
    
    class Config:
        from_attributes = True 
        orm_mode = True
    
    @validator('image_url', always=True)
    def build_image_url(cls, v, values):
        if 'image' in values and values['image']:
            base_url = settings.BACKEND_ADMIN_URL  
            return f"{base_url}/media/{values['image']}"
        return None