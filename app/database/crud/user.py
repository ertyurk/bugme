from datetime import datetime
from logging import log
from bson import ObjectId
from passlib.context import CryptContext

from app.schemas.user import *
from app.database.db import user_collection
from app.middlewares.auth.jwt_handler import signJWT


now = datetime.now()
hash_helper = CryptContext(schemes=["bcrypt"])


async def retrieve_users() -> dict:
    users = []
    async for user in user_collection.find():
        users.append(userEntity(user))
    return users


async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return userEntity(user)


async def create_user_helper(user_data: dict) -> dict:
    user = await user_collection.insert_one(
        {
            **user_data,
            "updated_at": str(datetime.now()),
            "created_at": str(datetime.now()),
        }
    )
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return userEntity(new_user)


async def update_user_data(id: str, data: dict) -> dict:
    # if update user data has included an email from another user,
    # we need to throw stop updating.
    user_exists = await user_collection.find_one({"email": data["email"]})
    if user_exists["_id"] != ObjectId(id):
        return False

    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user:
        data["updated_at"] = str(datetime.now())
        user_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


async def create_user(user_data: dict) -> dict:
    user_exists = await user_collection.find_one(
        {"email": user_data["email"]}, {"_id": 0}
    )
    if user_exists:
        return False

    user_data["password"] = hash_helper.encrypt(user_data["password"])
    new_user = await create_user_helper(user_data)
    return new_user


async def user_login(credentials: dict) -> dict:
    user = await user_collection.find_one(
        {"email": credentials["username"]}, {"_id": 0}
    )
    if user:
        password = hash_helper.verify(credentials["password"], user["password"])

        if password:
            return signJWT(credentials["username"])

        return False

    return False
