def slackEntity(slack) -> dict:
    return {
        "id": str(slack["_id"]),
        "app_id": slack["app_id"],
        "webhook": slack["webhook"],
        "status": slack["status"],
        "created_at": slack['created_at']
    }
