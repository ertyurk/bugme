def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "company": user["company"],
        "title": user["title"],
        "created_at": user['created_at']
    }
