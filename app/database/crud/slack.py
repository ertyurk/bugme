from datetime import datetime
from bson import ObjectId

from app.schemas.slack import *
from app.database.db import slack_collection
from app.database.crud.app import update_app_for_integration


async def retrieve_slacks() -> dict:
    slacks = []
    async for slack in slack_collection.find():
        slacks.append(slackEntity(slack))
    return slacks


async def retrieve_slack(id: str) -> dict:
    slack = await slack_collection.find_one({"_id": ObjectId(id)})
    if slack:
        return slackEntity(slack)


async def add_new_slack(slack_data: dict) -> dict:
    slack = await slack_collection.insert_one(
        {**slack_data, "created_at": str(datetime.now())}
    )
    new_slack = await slack_collection.find_one({"_id": ObjectId(slack.inserted_id)})
    await update_app_for_integration(slack_data["app_id"], "slack_integration", True)

    return slackEntity(new_slack)


async def update_slack_data(id: str, data: dict) -> dict:
    slack = await retrieve_slack(id)
    if slack:
        slack_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


async def retrieve_slack_integrations_of_an_app(app_id: str) -> dict:
    slacks = []
    async for slack in slack_collection.find({"app_id": app_id}):
        slacks.append(slackEntity(slack))
    return slacks


async def delete_integration(id: str) -> dict:
    slack = await slack_collection.find_one({"_id": ObjectId(id)})
    if slack:
        await slack_collection.delete_one({"_id": ObjectId(id)})
        return True
