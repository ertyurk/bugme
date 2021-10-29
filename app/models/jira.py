from typing import Optional
from pydantic import BaseModel, Field


class JiraModel(BaseModel):
    app_id: str = Field(...)
    issue_type: str = Field(...)
    email: str = Field(...)
    base_url: str = Field(...)
    api_key: str = Field(...)
    project_key: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "app_id": "60a6d09d2500c9e383db6e92",
                "issue_type": "10001",
                "email": "me@ertyurk.com",
                "base_url": "XXXX.atlassian.net",
                "api_key": "Vm83q1vrZMpBnq2MD0xHA2EE",
                "project_key": "UP",
            }
        }


class UpdateJiraModel(BaseModel):
    app_id: str = Field(...)
    issue_type: Optional[str]
    email: Optional[str]
    base_url: Optional[str]
    api_key: Optional[str]
    project_key: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "app_id": "60a6d09d2500c9e383db6e92",
                "issue_type": "10001",
                "email": "me@ertyurk.com",
                "base_url": "XXXX.atlassian.net",
                "api_key": "Vm83q1vrZMpBnq2MD0xHA2EE",
                "project_key": "UP",
            }
        }
