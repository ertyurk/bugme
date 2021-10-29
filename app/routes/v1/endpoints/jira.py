from fastapi import APIRouter, status, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.models.common import *
from app.models.jira import *
from app.database.crud.jira import *

router = APIRouter()


@router.get("/", response_description="jira integrations are retrieved.")
async def get_jira_integrations():
    jiras = await retrieve_jiras()
    return (
        ResponseModel(jiras, "jira integrations data retrieved successfully")
        if len(jiras) > 0
        else ResponseModel(jiras, "Empty list returned")
    )


@router.post(
    "/", response_description="jira integrations data added into the database."
)
async def add_jira_a_integration(jira: JiraModel = Body(...)):
    jira = jsonable_encoder(jira)
    new_jira = await add_new_jira(jira)
    return ResponseModel(
        new_jira,
        "jira integration created successfully.",
        status.HTTP_201_CREATED,
    )


@router.get("/{id}/", response_description="jira data retrieved.")
async def find_jira_integration(id):
    jira = await retrieve_jira(id)
    return (
        ResponseModel(jira, "jira integrations data retrieved successfully")
        if jira
        else ErrorResponseModel(
            "An error occured.", status.HTTP_404_NOT_FOUND, "Integration doesn't exist."
        )
    )


@router.put(
    "/{id}/", response_description="jira integrations data updated in the database."
)
async def update_a_jira_integration(id: str, jira: UpdateJiraModel = Body(...)):
    jira = jsonable_encoder(jira)
    updated_jira = await update_jira_data(id, jira)
    return (
        ResponseModel({"id": id}, "jira integration updated successfully")
        if updated_jira
        else ErrorResponseModel(
            "An error occurred",
            status.HTTP_404_NOT_FOUND,
            "There was an error updating the jira integration.",
        )
    )


@router.delete("/{id}/", response_description="Delete the integration")
async def delete_jira_integration(id: str):
    deleted_jira = await delete_integration(id)
    return (
        ResponseModel(
            "Integration with ID: {} removed".format(id),
            "Integration deleted successfully",
        )
        if deleted_jira
        else ErrorResponseModel(
            "An error occured",
            status.HTTP_404_NOT_FOUND,
            "Integration with id {0} doesn't exist".format(id),
        )
    )
