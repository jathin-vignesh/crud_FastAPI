from pydantic import BaseModel, EmailStr
from typing import Optional
class PersonCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class PersonUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class PersonResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True