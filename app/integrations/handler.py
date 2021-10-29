from app.database.crud.bug import retrieve_bug, update_bug_data_for_integration
from app.database.crud.app import retrive_apps_of_bundles
from app.integrations.jira import jira_integration
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
        if media["status"] != False:
            await run_integration(id)
        else:
            print(f"Unable to upload media for Bug ID: {id}")

    except Exception:
        print("Error: Background task faced with an error.")


async def run_integration(id: str) -> None:
    # Retrieve bug and check whether media uploaded or not.
    bug = await retrieve_bug(id)
    if not len(bug["media_path"]) > 0:
        print("INFO: There is no media uploaded for the bug, Integration passed.")
        raise Exception

    # Retrieve app data with bundle id
    apps = await retrive_apps_of_bundles(bug["bundle_id"], bug["platform"])

    if apps[0]:

        # try to send to clickup
        res = await clickup_integration(bug, apps[0])
        res = await slack_integration(res, apps[0])
        res = await jira_integration(res, apps[0])

        # finally, update the bug record
        await update_bug_data_for_integration(res)
        print(f"INFO: Bug data updated for ID: {res['id']}")

    else:
        print(f"INFO: There is no integration available for this bug")
