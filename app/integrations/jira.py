import requests
from requests.auth import HTTPBasicAuth
import json

from app.database.crud.jira import retrieve_jira_integrations_of_an_app


async def jira_integration(data: dict, app: dict) -> dict:
    try:
        if not app["jira_integration"] != False:
            print(f"INFO: Jira Integration is disabled for App: {app['id']}")
            raise Exception

        # Create jira task if it wasn't created.
        if not data["sent_to_jira"] != True:
            print(f"INFO: Jira task already created Bug: {data['id']}")
            raise Exception

        jira_config = await retrieve_jira_integrations_of_an_app(app["id"])
        jira_task = await create_jira_task(data, jira_config[0])

        if not jira_task["status"] == 201:
            print(
                f"Jira task creation request received an error from Jira: {jira_task}"
            )
            raise Exception

        print(
            f"INFO: Jira task created for the task as {jira_task['response']['self']} \
                - #{jira_task['response']['id']} for Bug ID: {data['id']}"
        )

        data["sent_to_jira"] = True
        data["jira_task_url"] = jira_task["response"]["self"]

        return data
    except:
        return data


async def create_jira_task(data: dict, config: dict) -> dict:

    description = f"""
        Description: {data['description']} 

        Platform: {data['platform']} 
        Device: {data['device']} 
        Location: {data['location']} 
        Screen size: {data['screen_size']} 
        App version: {data['app_version']} 
        Bundle ID: {data['bundle_id']} 
        Branch: {data['branch']} 
        
        Locale: {data['locale']}
        Density: {data['density']}
        Session duration: {data['session_duration']} 
        
        Media: {data['media_path']} 

        User data: {data['user_data']}
        Console log: {data['console_log']}
        Reporter: {data['reporter_email']} 
        Report date: {data['created_at']}
        """

    payload = json.dumps(
        {
            "fields": {
                "summary": f"{data['category']} | {data['title']}",
                "issuetype": {"id": "10001"},
                "project": {"key": config["project_key"]},
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [{"text": description, "type": "text"}],
                        }
                    ],
                },
            }
        }
    )

    auth = HTTPBasicAuth(config["email"], config["api_key"])
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    r = requests.post(
        f"https://{config['base_url']}/rest/api/3/issue",
        headers=headers,
        data=payload,
        auth=auth,
    )
    return {"status": r.status_code, "response": r.json()}
