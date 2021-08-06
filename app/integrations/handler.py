from app.database.crud.bug import retrieve_bug, update_bug_data_for_integration
from app.database.crud.app import retrive_apps_of_bundles
from app.integrations.slack import slack_integration
from app.integrations.clickup import clickup_integration
from app.middlewares.helpers.media_helper import media_wrapper


"""
	Once media uploaded to the cloud, we will run the integrations
"""


async def main_background_task_handler(id: str, files) -> None:
    try:
        # upload medias to the cloud for correspondent bug Id
        media = await media_wrapper(id, files)

        # run integrations if media uploaded successfully.
        if media['status'] != False:
            bug = await retrieve_bug(id)
            await run_integration(bug)
        else:
            print(f"Unable to upload media for Bug ID: {id}")
            
    except Exception:
        print('Error: Background task faced with an error.')


async def run_integration(data: dict) -> None:
    # check whether media uploaded or not.
    if len(data['media_path']) > 0:
        # Retrieve app data with bundle id
        apps = await retrive_apps_of_bundles(data['bundle_id'])
        if apps[0]:

            res = await clickup_integration(data, apps[0])
            res = await slack_integration(data, apps[0])

            # finally, update the bug record
            await update_bug_data_for_integration(res)
            print(f"INFO: Bug data updated for ID: {res['id']}")

    else:
        print("INFO: There is no media uploaded for the bug, Integration passed.")
