def brandEntity(brands) -> dict:
    return {
        "id": str(brands["_id"]),
        "brand": brands["brand"],
        "auth_key": brands["auth_key"],
        "user_id": brands["user_id"],
        "created_at": brands["created_at"],
    }
