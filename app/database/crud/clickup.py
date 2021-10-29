from datetime import datetime
from bson import ObjectId

from app.schemas.clickup import *
from app.database.db import clickup_collection
from app.database.crud.app import update_app_for_integration


async def retrieve_clickups() -> dict:
    clickups = []
    async for clickup in clickup_collection.find():
        clickups.append(clickupEntity(clickup))
    return clickups


async def retrieve_clickup(id: str) -> dict:
    clickup = await clickup_collection.find_one({"_id": ObjectId(id)})
    if clickup:
        return clickupEntity(clickup)


async def add_new_clickup(clickup_data: dict) -> dict:
    clickup = await clickup_collection.insert_one(
        {**clickup_data, "created_at": str(datetime.now())}
    )
    new_clickup = await clickup_collection.find_one({"_id": clickup.inserted_id})
    await update_app_for_integration(
        clickup_data["app_id"], "clickup_integration", True
    )
    return clickupEntity(new_clickup)


async def update_clickup_data(id: str, data: dict) -> dict:
    clickup = await clickup_collection.find_one({"_id": ObjectId(id)})
    if clickup:
        clickup_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


async def retrieve_clickup_integrations_of_an_app(app_id: str) -> dict:
    clickups = []
    async for clickup in clickup_collection.find({"app_id": app_id}):
        clickups.append(clickupEntity(clickup))
    return clickups


async def delete_integration(id: str) -> dict:
    clickup = await clickup_collection.find_one({"_id": ObjectId(id)})
    if clickup:
        await clickup_collection.delete_one({"_id": ObjectId(id)})
        return True
