from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    company: str = Field(...)
    title: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "email": "me@ertyurk.com",
                "password": "qweasd123!",
                "company": "Lean Scale",
                "title": "Product Manager"
            }
        }


class UpdateUserModel(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]
    company: Optional[str]
    title: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "email": "me@ertyurk.com",
                "password": "qweasd123!",
                "company": "Lean Scale",
                "title": "Product Manager"
            }
        }
