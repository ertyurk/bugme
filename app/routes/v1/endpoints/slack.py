from fastapi import APIRouter, status, Body
from fastapi.encoders import jsonable_encoder

from app.models.common import *
from app.models.slack import *
from app.database.crud.slack import *

router = APIRouter()


@router.get("/", response_description="All Slack integrations list is retrieved.")
async def get_slack_integration_records():
    slacks = await retrieve_slacks()
    return (
        ResponseModel(slacks, "Slack integrations retrieved successfully")
        if len(slacks) > 0
        else ResponseModel(slacks, "Empty list returned")
    )


@router.post("/", response_description="Slack integration added into the database.")
async def add_a_slack_integration(slack: SlackModel = Body(...)):
    print(slack)
    new_slack = await add_new_slack(jsonable_encoder(slack))
    return ResponseModel(
        new_slack, "slack integration created successfully.", status.HTTP_201_CREATED
    )


@router.get("/{id}/", response_description="slack data retrieved.")
async def find_a_slack_integration(id):
    slack = await retrieve_slack(id)
    return (
        ResponseModel(slack, "slack data retrieved successfully")
        if slack
        else ErrorResponseModel("An error occured.", 404, "slack doesn't exist.")
    )


@router.put(
    "/{id}/", response_description="Slack integration data updated in the database."
)
async def update_a_slack_integration(id: str, slack: UpdateSlackModel = Body(...)):
    slack = jsonable_encoder(slack)
    updated_slack = await update_slack_data(id, slack)
    return (
        ResponseModel({"id": id}, "Slack integration updated successfully")
        if updated_slack
        else ErrorResponseModel(
            "An error occurred",
            status.HTTP_404_NOT_FOUND,
            "There was an error updating the Slack integration.",
        )
    )


@router.delete("/{id}/", response_description="Delete the integration")
async def delete_slack_integration(id: str):
    deleted_slack = await delete_integration(id)
    return (
        ResponseModel(
            "Integration with ID: {} removed".format(id),
            "Integration deleted successfully",
        )
        if deleted_slack
        else ErrorResponseModel(
            "An error occured", 404, "Integration with id {0} doesn't exist".format(id)
        )
    )
