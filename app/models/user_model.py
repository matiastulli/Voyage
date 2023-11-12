from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    last_name: str
    mail: EmailStr
    password: str
    id_role: int

    class Config:
        orm_mode = True

class UserRead(BaseModel):
    mail: EmailStr
    password: str

    class Config:
        orm_mode = True
