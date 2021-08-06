from typing import Optional
from pydantic import BaseModel, Field


class ClickupModel(BaseModel):
    app_id: str = Field(...)
    client: Optional[str]
    secret: Optional[str]
    team_token: Optional[str]
    code: Optional[str]
    auth_key: Optional[str]
    assigned_user: str = Field(...)
    assigned_status: str = Field(...)
    task_list_id: str = Field(...)
    task_label: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "app_id": "60a6d09d2500c9e383db6e92",
                "client": "--not ready to use--",
                "secret": "--not ready to use--",
                "team_token": "not ready to use",
                "code": "not ready to use",
                "auth_key": "pk_3606225_QP7Y2WXXM6SHICC9Z9UKZI2K4XIO9RFO",
                "assigned_user": "3606225",
                "assigned_status": "OPEN",
                "task_list_id": "44623749",
                "task_label": "LS Bugger Reporter",
            }
        }


class UpdateClickupModel(BaseModel):
    app_id: str = Field(...)
    client: Optional[str]
    secret: Optional[str]
    team_token: Optional[str]
    code: Optional[str]
    auth_key: Optional[str]
    assigned_user: Optional[str]
    assigned_status: Optional[str]
    task_list_id: Optional[str]
    task_label: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "app_id": "60a6d09d2500c9e383db6e92",
                "client": "--not ready to use--",
                "secret": "--not ready to use--",
                "team_token": "not ready to use",
                "code": "not ready to use",
                "auth_key": "pk_3606225_QP7Y2WXXM6SHICC9Z9UKZI2K4XIO9RFO",
                "assigned_user": "3606225",
                "assigned_status": "OPEN",
                "task_list_id": "44623749",
                "task_label": "LS Bugger Reporter",
            }
        }
