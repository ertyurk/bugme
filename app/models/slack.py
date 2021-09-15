from typing import Optional
from pydantic import BaseModel, Field


class SlackModel(BaseModel):
    app_id: str = Field(...)
    webhook: str = Field(...)
    status: bool = False
    created_at: Optional[str]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "app_id": "60a6d09d2500c9e383db6e92",
                "webhook": "https://hooks.slack.com/services/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",
                "status": False,
            }
        }


class UpdateSlackModel(BaseModel):
    app_id: Optional[str]
    webhook: Optional[str]
    status: Optional[bool]
    created_at: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "app_id": "60a6d09d2500c9e383db6e92",
                "webhook": "https://hooks.slack.com/services/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",
                "status": False,
            }
        }
