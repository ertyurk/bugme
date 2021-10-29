from datetime import datetime
from bson import ObjectId
from app.schemas.app import *
from app.database.db import apps_collection


async def retrieve_apps() -> dict:
    apps = []
    async for app in apps_collection.find():
        apps.append(appEntity(app))
    return apps


async def add_new_app(app_data: dict) -> dict:
    # convert platform type to upper case
    app_data["platform"] = app_data["platform"].upper()
    app = await apps_collection.insert_one(
        {**app_data, "created_at": str(datetime.now())}
    )
    new_app = await apps_collection.find_one({"_id": app.inserted_id})
    return appEntity(new_app)


async def retrieve_app(id: str) -> dict:
    app = await apps_collection.find_one({"_id": ObjectId(id)})
    if app:
        return appEntity(app)


async def update_app_for_integration(id: str, key: str, value: str) -> dict:
    app = await apps_collection.find_one({"_id": ObjectId(id)})
    if app:
        app[key] = value
        apps_collection.update_one({"_id": ObjectId(id)}, {"$set": app})
        return True
    return False


async def update_app_data(id: str, data: dict) -> dict:
    # convert platform type to upper case
    if data["platform"]:
        data["platform"] = data["platform"].upper()

    app = await apps_collection.find_one({"_id": ObjectId(id)})
    if app:
        apps_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True
    return False


async def retrive_apps_of_user(id: str) -> dict:
    apps = []
    async for app in apps_collection.find({"user_id": id}):
        apps.append(appEntity(app))
    return apps


async def retrive_apps_of_brand(id: str) -> dict:
    apps = []
    async for app in apps_collection.find({"brand_id": id}):
        apps.append(appEntity(app))
    return apps


async def retrive_apps_of_bundles(id: str, platform: str) -> dict:
    apps = []
    async for app in apps_collection.find({"bundle_id": id, "platform": platform}):
        apps.append(appEntity(app))
    return apps
