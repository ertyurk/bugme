from typing import Optional
from pydantic import BaseModel, Field


class AppsModel(BaseModel):
    brand_id: str = Field(...)
    user_id: str = Field(...)
    bundle_id: str = Field(...)
    platform: str = Field(...)
    slack_integration: bool = False
    clickup_integration: bool = False
    jira_integration: bool = False

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "brand_id": "60a6c72d470fa98f64464cbc",
                "user_id": "60a57e1d1201f43c9c51c044",
                "bundle_id": "aaa.bbb.ccc.beta",
                "platform": "Android",
                "slack_integration": False,
                "clickup_integration": False,
                "jira_integration": False,
            }
        }


class UpdateAppsModel(BaseModel):
    brand_id: Optional[str]
    user_id: Optional[str]
    bundle_id: Optional[str]
    platform: Optional[str]
    slack_integration: Optional[bool]
    clickup_integration: Optional[bool]
    jira_integration: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "brand_id": "60a6c72d470fa98f64464cbc",
                "user_id": "60a57e1d1201f43c9c51c044",
                "bundle_id": "aaa.bbb.ccc.beta",
                "platform": "Android",
                "slack_integration": False,
                "clickup_integration": False,
                "jira_integration": False,
            }
        }
