from pydantic import BaseModel,validator
from typing import Optional
from config.settings import settings

class CustomUserSchema(BaseModel):
    id: int
    image: str
    is_worker: bool
    first_name: str | None = None
    last_name: str | None = None
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