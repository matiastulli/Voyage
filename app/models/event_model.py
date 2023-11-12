from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    description: str
    status: str
    id_user: int

class EventResponse(BaseModel):
    id: int
    description: str
    status: str
    id_user: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
