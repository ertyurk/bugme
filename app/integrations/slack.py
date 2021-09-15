import requests

from app.database.crud.slack import retrieve_slack_integrations_of_an_app


async def slack_integration(data: dict, app: dict) -> dict:
    try:
        if not app["slack_integration"] == True:
            print(f"INFO: Slack integration is disabled for App: {app['id']}")
            raise Exception

            # Send clickup message if it wasn't sent.
        if not data["sent_to_slack"] != True:
            print(f"INFO: Slack message sent already for Bug: {data['id']}")
            raise Exception

        slack_config = await retrieve_slack_integrations_of_an_app(app["id"])

        if not slack_config[0]["status"] == True:
            print(
                f"INFO: Slack status is disabled for Slack Integration: {slack_config[0]['id']}"
            )
            raise Exception

        slack_sender = await send_slack_msg(slack_config[0]["webhook"], data)

        if not slack_sender["status"] == 200:
            print(f"INFO: Slack message request received an error from SLACK")
            raise Exception

        print(
            f"INFO: Slack message sent for the task: {data['title']} for the Bug ID: {data['id']}"
        )
        data["sent_to_slack"] = True
        return data
    except:
        return data


async def send_slack_msg(hook: str, data: dict) -> dict:
    headers = {
        "Content-type": "application/json",
    }
    payload = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": f":fire: New {data['platform']} bug reported!",
                    "emoji": True,
                },
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*{data['title']}*"},
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "See in the clickup",
                        "emoji": True,
                    },
                    "style": "primary",
                    "url": data["clickup_task_url"],
                    "action_id": "button-action",
                },
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"{data['description']}"},
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "plain_text",
                        "text": f"Reporter: {data['reporter_email']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"App version: {data['app_version']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"Bundle: {data['bundle_id']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"Branch: {data['branch']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"Device: {data['device']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"Session: {data['session_duration']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"Screen Size: {data['screen_size']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"Location: {data['location']}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f"Report date: {data['created_at']}",
                        "emoji": True,
                    },
                ],
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": f"First media from total {len(data['media_path'])} uploaded",
                    "emoji": True,
                },
                "image_url": data["media_path"][0],
                "alt_text": f"1/{len(data['media_path'])}",
            },
        ]
    }

    r = requests.post(hook, json=payload, headers=headers)
    return {
        "status": r.status_code,
    }
