def clickupEntity(clickup) -> dict:
    return {
        "id": str(clickup["_id"]),
        "app_id": clickup["app_id"],
        "client": clickup["client"],
        "secret": clickup["secret"],
        "team_token": clickup["team_token"],
        "code": clickup["code"],
        "auth_key": clickup["auth_key"],
        "assigned_user": clickup["assigned_user"],
        "assigned_status": clickup["assigned_status"],
        "task_list_id": clickup["task_list_id"],
        "task_label": clickup["task_label"],
        "created_at": clickup['created_at']
    }
