from datetime import date, datetime

from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    email: EmailStr
    phone: str = Field(default='+380123456789')
    birthday: date


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    email: EmailStr
    phone: str = Field(default='+380123456789')
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
