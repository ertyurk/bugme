from sys import platform
from typing import Optional
from pydantic import BaseModel, Field


class BugModel(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    platform: str = Field(...)
    reporter_email: str = Field(...)
    category: str = Field(...)
    app_version: str = Field(...)
    bundle_id: str = Field(...)
    branch: str = Field(...)
    device: str = Field(...)
    location: str = Field(...)
    session_duration: str = Field(...)
    screen_size: str = Field(...)
    density: Optional[str]
    user_data: Optional[str]
    console_log: Optional[str]
    locale: str = Field(...)
    media_path: Optional[list]
    clickup_task_url: Optional[str]
    reported_at: str = Field(...)
    sent_to_clickup: bool = False
    sent_to_slack: bool = False

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "bundle_id": "com.dcafood.leanscale.alpha",
                "platform": "ANDROID",
                "title": "PDP video glitch",
                "description": "Pass the onboarding, navigate from homebase to shop, click to the any product. Observe: There is a video without tumbnail",
                "reporter_email": "mehmet@leanscale.com",
                "category": "Bug",
                "app_version": "1.11.19",
                "branch": "RC1119",
                "device": "CLT-AL00",
                "location": "tr",
                "session_duration": "345ms",
                "screen_size": "1080x2240",
                "density": "5",
                "user_data": '{"id":32082,"group_id":1,"created_at":"2020-05-13T13:25:26Z","updated_at":"2021-04-13T11:25:27Z","created_in":"La3eb English","email":"erturk@leanscale.com","firstname":"Mehmet","lastname":"Erturk","gender":0,"store_id":27,"website_id":3,"addresses":[{"id":18320,"customer_id":32082,"region":{"region_code":null,"region":null,"region_id":0},"region_id":0,"country_id":"SA","street":["gdfgdfg"],"telephone":"966591826195","postcode":"Abaha aljadida - \u0623\u0628\u0647\u0627 \u0627\u0644\u062c\u062f\u064a\u062f\u0647","city":"Abha- \u0623\u0628\u0647\u0627","firstname":"mehmet","lastname":"erturrk"}]}',
                "console_log": "any console log here",
                "locale": "en",
                "reported_at": "ISO£23452345",
            }
        }


class UpdateBugModel(BaseModel):
    brand_id: Optional[str]
    platform: Optional[str]
    title: Optional[str]
    description: Optional[str]
    reporter_email: Optional[str]
    category: Optional[str]
    app_version: Optional[str]
    bundle_id: Optional[str]
    branch: Optional[str]
    device: Optional[str]
    location: Optional[str]
    session_duration: Optional[str]
    screen_size: Optional[str]
    density: Optional[str]
    user_data: Optional[str]
    console_log: Optional[str]
    locale: Optional[str]
    media_path: Optional[str]
    clickup_task_url: Optional[str]
    reported_at: Optional[str]
    sent_to_clickup: Optional[bool]
    sent_to_slack: Optional[bool]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "brand_id": "60a6c72d470fa98f64464cbc",
                "bundle_id": "com.dcafood.leanscale.alpha",
                "sent_to_clickup": False,
                "sent_to_slack": False,
                "title": "PDP video glitch",
                "description": "Pass the onboarding, navigate from homebase to shop, click to the any product. Observe: There is a video without tumbnail",
                "reporter_email": "mehmet@leanscale.com",
                "category": "Bug",
                "app_version": "1.11.19",
                "branch": "RC1119",
                "device": "CLT-AL00",
                "location": "tr",
                "session_duration": "345ms",
                "screen_size": "1080x2240",
                "density": "5",
                "user_data": '{"id":32082,"group_id":1,"created_at":"2020-05-13T13:25:26Z","updated_at":"2021-04-13T11:25:27Z","created_in":"La3eb English","email":"erturk@leanscale.com","firstname":"Mehmet","lastname":"Erturk","gender":0,"store_id":27,"website_id":3,"addresses":[{"id":18320,"customer_id":32082,"region":{"region_code":null,"region":null,"region_id":0},"region_id":0,"country_id":"SA","street":["gdfgdfg"],"telephone":"966591826195","postcode":"Abaha aljadida - \u0623\u0628\u0647\u0627 \u0627\u0644\u062c\u062f\u064a\u062f\u0647","city":"Abha- \u0623\u0628\u0647\u0627","firstname":"mehmet","lastname":"erturrk"}]}',
                "console_log": "any console log here",
                "locale": "en",
                "reported_at": "ISO£23452345",
            }
        }
