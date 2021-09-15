def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "company": user["company"],
        "title": user["title"],
        "admin": user["admin"],
        "is_active": user["is_active"],
        "updated_at": user["updated_at"],
        "created_at": user["created_at"],
    }
