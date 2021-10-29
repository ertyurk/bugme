from fastapi import APIRouter, status, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.models.common import *
from app.models.clickup import *
from app.database.crud.clickup import *

router = APIRouter()


@router.get("/", response_description="Clickup integrations are retrieved.")
async def get_clickup_integrations():
    clickups = await retrieve_clickups()
    return (
        ResponseModel(clickups, "Clickup integrations data retrieved successfully")
        if len(clickups) > 0
        else ResponseModel(clickups, "Empty list returned")
    )


@router.post(
    "/", response_description="Clickup integrations data added into the database."
)
async def add_clickup_a_integration(clickup: ClickupModel = Body(...)):
    clickup = jsonable_encoder(clickup)
    new_clickup = await add_new_clickup(clickup)
    return ResponseModel(
        new_clickup,
        "clickup integration created successfully.",
        status.HTTP_201_CREATED,
    )


@router.get("/{id}/", response_description="Clickup data retrieved.")
async def find_clickup_integration(id):
    clickup = await retrieve_clickup(id)
    return (
        ResponseModel(clickup, "Clickup integrations data retrieved successfully")
        if clickup
        else ErrorResponseModel(
            "An error occured.", status.HTTP_404_NOT_FOUND, "Integration doesn't exist."
        )
    )


@router.put(
    "/{id}/", response_description="Clickup integrations data updated in the database."
)
async def update_a_clickup_integration(
    id: str, clickup: UpdateClickupModel = Body(...)
):
    clickup = jsonable_encoder(clickup)
    updated_clickup = await update_clickup_data(id, clickup)
    return (
        ResponseModel({"id": id}, "Clickup integration updated successfully")
        if updated_clickup
        else ErrorResponseModel(
            "An error occurred",
            status.HTTP_404_NOT_FOUND,
            "There was an error updating the Clickup integration.",
        )
    )


@router.delete("/{id}/", response_description="Delete the integration")
async def delete_clickup_integration(id: str):
    deleted_clickup = await delete_integration(id)
    return (
        ResponseModel(
            "Integration with ID: {} removed".format(id),
            "Integration deleted successfully",
        )
        if deleted_clickup
        else ErrorResponseModel(
            "An error occured",
            status.HTTP_404_NOT_FOUND,
            "Integration with id {0} doesn't exist".format(id),
        )
    )
