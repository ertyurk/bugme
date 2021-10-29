def jiraEntity(jira) -> dict:
    return {
        "id": str(jira["_id"]),
        "app_id": jira["app_id"],
        "issue_type": jira["issue_type"],
        "email": jira["email"],
        "project_key": jira["project_key"],
        "base_url": jira["base_url"],
        "api_key": jira["api_key"],
        "created_at": jira["created_at"],
    }
