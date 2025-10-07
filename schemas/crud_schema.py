from pydantic import BaseModel, EmailStr

class PersonCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class PersonResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True