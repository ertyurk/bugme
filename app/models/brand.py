from typing import Optional
from pydantic import BaseModel, Field


class BrandModel(BaseModel):
    brand: str = Field(...)
    auth_key: Optional[str]
    user_id: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "brand": "Lean Scale Bugger",
                "user_id": "60a57e1d1201f43c9c51c044"
            }
        }


class UpdateBrandModel(BaseModel):
    brand: Optional[str]
    auth_key: Optional[str]
    user_id: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "brand": "Lean Scale Bugger",
                "user_id": "60a57e1d1201f43c9c51c044"
            }
        }
