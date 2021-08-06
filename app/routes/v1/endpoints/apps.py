from fastapi import APIRouter, status, Body
from fastapi.encoders import jsonable_encoder

from app.models.common import *
from app.models.app import *
from app.database.crud.app import *

from app.database.crud.bug import retrive_bugs_from_bundle
from app.database.crud.clickup import retrieve_clickup_integrations_of_an_app
from app.database.crud.slack import retrieve_slack_integrations_of_an_app

router = APIRouter()


@router.get('/', response_description="apps are retrieved.")
async def get_apps():
    apps = await retrieve_apps()
    return ResponseModel(apps, "apps data retrieved successfully") \
        if len(apps) > 0 \
        else ResponseModel(
        apps, "Empty list returned"
    )


@router.post('/', response_description="apps data added into the database.")
async def add_app(app: AppsModel = Body(...)):
    app = jsonable_encoder(app)
    new_app = await add_new_app(app)
    return ResponseModel(new_app, "app created successfully.", status.HTTP_201_CREATED)


@router.get("/{id}", response_description="app data retrieved.")
async def get_app(id):
    app = await retrieve_app(id)
    return ResponseModel(app, "app data retrieved successfully") \
        if app \
        else ErrorResponseModel("An error occured.", status.HTTP_404_NOT_FOUND, "App doesn't exist.")


@router.put('/{id}', response_description="App data updated in the database.")
async def update_app(id: str, app: UpdateAppsModel = Body(...)):
    app = jsonable_encoder(app)
    updated_app = await update_app_data(id, app)
    return ResponseModel({"id": id},
                         "App updated successfully") \
        if updated_app \
        else ErrorResponseModel("An error occurred", status.HTTP_404_NOT_FOUND, "There was an error updating the App.")


@router.get("/bundle/bugs", response_description="Bugs retrieved from a brand of an app.")
async def get_apps_of_brand(bundle_id: str, brand_id: str):
    bugs = await retrive_bugs_from_bundle(bundle_id, brand_id)
    return ResponseModel(bugs, "Brand data retrieved successfully") \
        if bugs \
        else ErrorResponseModel("An error occured.", status.HTTP_404_NOT_FOUND, "Brand doesn't exist.")


@router.get("/integrations/slack", response_description="Slack integrations retrieved from brand.")
async def retrieve_slack_integrations_of_the_app(app_id: str):
    clickups = await retrieve_slack_integrations_of_an_app(app_id)
    return ResponseModel(clickups, f"Slack integration are retrieved successfully for the App ID: {app_id}") \
        if clickups \
        else ErrorResponseModel("An error occured.", status.HTTP_404_NOT_FOUND, "Integration doesn't exist.")


@router.get("/integrations/clickup", response_description="Clickup integrations retrieved from App.")
async def retrieve_clickup_integrations_of_the_app(app_id: str):
    clickups = await retrieve_clickup_integrations_of_an_app(app_id)
    return ResponseModel(clickups, f"Clickup integration are retrieved successfully for the App ID: {app_id}") \
        if clickups \
        else ErrorResponseModel("An error occured.", status.HTTP_404_NOT_FOUND, "Integration doesn't exist.")
