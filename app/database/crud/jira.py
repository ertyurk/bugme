from fastapi import BackgroundTasks
from datetime import datetime
from bson import ObjectId

from app.schemas.jira import *
from app.database.db import jira_collection
from app.database.crud.app import update_app_for_integration


async def retrieve_jiras() -> dict:
    jiras = []
    async for jira in jira_collection.find():
        jiras.append(jiraEntity(jira))
    return jiras


async def retrieve_jira(id: str) -> dict:
    jira = await jira_collection.find_one({"_id": ObjectId(id)})
    if jira:
        return jiraEntity(jira)


async def add_new_jira(jira_data: dict) -> dict:
    jira = await jira_collection.insert_one(
        {**jira_data, "created_at": str(datetime.now())}
    )
    new_jira = await jira_collection.find_one({"_id": jira.inserted_id})
    await update_app_for_integration(jira_data["app_id"], "jira_integration", True)

    return jiraEntity(new_jira)


async def update_jira_data(id: str, data: dict) -> dict:
    jira = await jira_collection.find_one({"_id": ObjectId(id)})
    if jira:
        jira_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


async def retrieve_jira_integrations_of_an_app(app_id: str) -> dict:
    jiras = []
    async for jira in jira_collection.find({"app_id": app_id}):
        jiras.append(jiraEntity(jira))
    return jiras


async def delete_integration(id: str) -> dict:
    print(id)
    jira = await jira_collection.find_one({"_id": ObjectId(id)})
    print(jira)
    if jira:
        await jira_collection.delete_one({"_id": ObjectId(id)})
        return True
