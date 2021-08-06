def appEntity(apps) -> dict:
    return {
        "id": str(apps["_id"]),
        "brand_id": apps["brand_id"],
        "user_id": apps["user_id"],
        "bundle_id": apps["bundle_id"],
        "platform": apps["platform"],
        "slack_integration": apps["slack_integration"],
        "clickup_integration": apps["clickup_integration"],
        "created_at": apps['created_at']
    }
