from datetime import datetime
from bson import ObjectId

from app.schemas.brand import *
from app.middlewares.helpers.api_key_helper import generate_api_key
from app.database.db import brand_collection


async def retrieve_brands():
    brands = []
    async for brand in brand_collection.find():
        brands.append(brandEntity(brand))
    return brands


async def add_new_brand(brand_data: dict) -> dict:
    brand = await brand_collection.insert_one(
        {
            **brand_data,
            "auth_key": generate_api_key(),
            "created_at": str(datetime.now()),
        }
    )
    new_brand = await brand_collection.find_one({"_id": brand.inserted_id})
    return brandEntity(new_brand)


async def retrieve_brand(id: str) -> dict:
    brand = await brand_collection.find_one({"_id": ObjectId(id)})
    if brand:
        return brandEntity(brand)


async def update_brand_data(id: str, data: dict) -> dict:
    brand = await brand_collection.find_one({"_id": ObjectId(id)})
    if brand:
        brand_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


async def update_brand_api_key(id: str) -> dict:
    brand = await brand_collection.find_one({"_id": ObjectId(id)})
    brand["auth_key"] = generate_api_key()
    if brand:
        brand_collection.update_one({"_id": ObjectId(id)}, {"$set": brand})
        return {"id": id, "brand": brand["brand"], "auth_key": brand["auth_key"]}


async def retrive_brands_of_user(id: str) -> dict:
    brands = []
    async for brand in brand_collection.find({"user_id": id}):
        brands.append(brandEntity(brand))
    return brands


async def retrieve_brand_from_auth_key(auth_key: str) -> dict:
    brand = await brand_collection.find_one({"auth_key": auth_key})
    if brand:
        return brandEntity(brand)
