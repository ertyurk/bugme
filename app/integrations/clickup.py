import requests

from app.database.crud.clickup import retrieve_clickup_integrations_of_an_app


async def clickup_integration(data: dict, app: dict) -> dict:
    if app['clickup_integration'] != False:
        # Create clickup task if it wasn't created.
        if data['sent_to_clickup'] != True:
            cu_config = await retrieve_clickup_integrations_of_an_app(app['id'])
            cu_task = await create_clickup_task(data, cu_config[0])

            # If the status is 200 for slack integration
            # append cu_task url and update sent_to_clickup calue

            if cu_task['status'] == 200:
                print(
                    f"INFO: Clickup task created for the task as {cu_task['response']['name']} - #{cu_task['response']['id']} for Bug ID: {data['id']}")
                data['sent_to_clickup'] = True
                data['clickup_task_url'] = cu_task['response']['url']
            else:
                print(
                    f"Clickup task creation request received an error from Clickup", cu_task)
        else:
            print(
                f"INFO: Clickup task already created Bug: {data['id']}")
    else:
        print(
            f"INFO: Clickup Integration is disabled for App: {app['id']}")

    return data


async def create_clickup_task(data: dict, config: dict) -> dict:
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

    payload = {
        "name": f"{data['category']} | {data['title']}",
        "description": description,
        "tags": [f"{data['platform']}"],
        "status": "IMPORTED"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": config['auth_key']
    }

    r = requests.post(f"https://api.clickup.com/api/v2/list/{config['task_list_id']}/task",
                      json=payload,
                      headers=headers)

    return {
        'status': r.status_code,
        'response': r.json()
    }
