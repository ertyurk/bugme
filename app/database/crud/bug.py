from datetime import datetime
from bson import ObjectId

from app.schemas.bug import *
from app.database.db import bug_collection
from app.middlewares.helpers.bug_helpers import bundle_id_handler


async def retrieve_bugs() -> dict:
    bugs = []
    async for bug in bug_collection.find():
        bugs.append(bugEntity(bug))
    return bugs


async def add_new_bug(bug_data: dict, authorization: str) -> dict:
    if authorization[0:3] == "pk_":
        bug = await bundle_id_handler(auth_key=authorization, bug_data=bug_data)
    else:
        bug = bug_data
    pre_bug = await bug_collection.insert_one(
        {**bug, "created_at": str(datetime.now())}
    )
    new_bug = await bug_collection.find_one({"_id": pre_bug.inserted_id})
    return bugEntity(new_bug)


async def retrieve_bug(id: str) -> dict:
    bug = await bug_collection.find_one({"_id": ObjectId(id)})
    if bug:
        return bugEntity(bug)


async def update_bug_data_for_media(id: str, media: list) -> bool:
    bug = await bug_collection.find_one({"_id": ObjectId(id)})
    bug["media_path"] = media
    if bug:
        bug_collection.update_one({"_id": ObjectId(id)}, {"$set": bug})
        return True
    else:
        return False


async def update_bug_data_for_integration(data: dict) -> bool:
    bug = await bug_collection.find_one({"_id": ObjectId(data["id"])})
    if bug:
        bug_collection.update_one({"_id": ObjectId(data["id"])}, {"$set": data})
        return True
    else:
        return False


async def retrive_bugs_of_brand(id: str) -> dict:
    bugs = []
    async for bug in bug_collection.find({"brand_id": id}):
        bugs.append(bugEntity(bug))
    return bugs


async def retrive_bugs_from_bundle(bundle_id: str, brand_id: str) -> dict:
    bugs = []
    async for bug in bug_collection.find(
        {"bundle_id": bundle_id, "brand_id": brand_id}
    ):
        bugs.append(bugEntity(bug))
    return bugs
