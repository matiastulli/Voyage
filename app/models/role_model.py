from pydantic import BaseModel

class RoleCreate(BaseModel):
    description: str

    class Config:
        orm_mode = True
        
class RoleUpdate(BaseModel):
    id: int
    description: str