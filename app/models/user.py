from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    company: str = Field(...)
    title: str = Field(...)
    admin: bool = Field(...)
    is_active: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "email": "me@ertyurk.com",
                "password": "qweasd123!",
                "company": "Lean Scale",
                "title": "Product Manager",
                "admin": True,
                "is_active": True,
            }
        }


class UpdateUserModel(BaseModel):
    email: Optional[EmailStr]
    company: Optional[str]
    title: Optional[str]
    admin: Optional[bool]
    is_active: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "email": "me@ertyurk.com",
                "company": "Lean Scale",
                "title": "Product Manager",
                "admin": True,
                "is_active": True,
            }
        }
