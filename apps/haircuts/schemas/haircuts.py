from pydantic import BaseModel

class HairCutSchema(BaseModel):
    id: int
    name: str
    small_description: str
    price: float

    class Config:
        from_attributes = True
        orm_mode = True
