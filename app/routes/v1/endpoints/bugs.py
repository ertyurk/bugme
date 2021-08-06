from fastapi import APIRouter, status, Body, Header, File, UploadFile, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from typing import List

from app.models.common import *
from app.models.bug import *
from app.database.crud.bug import *
from app.integrations.handler import main_background_task_handler


router = APIRouter()


@router.get('/', response_description="Bugs are retrieved.")
async def get_bugs():
    bugs = await retrieve_bugs()
    return ResponseModel(bugs, "bugs data retrieved successfully") \
        if len(bugs) > 0 \
        else ResponseModel(
        bugs, "Empty list returned"
    )


@router.post('/', response_description="Bugs data added into the database.")
async def add_bug(bug: BugModel = Body(...), authorization: Optional[str] = Header(None)):
    bug = jsonable_encoder(bug)
    new_bug = await add_new_bug(bug, authorization[7:])
    return ResponseModel(new_bug, "Bug created successfully.", status.HTTP_201_CREATED)


@router.post("/{id}/media/")
async def upload_files(bg_task: BackgroundTasks, id: str, files: List[UploadFile] = File(...)):
    # Background task will upload files, create clickup task,
    # upload files to clickup as well then will send slack message.
    bg_task.add_task(main_background_task_handler, id, files)
    return ResponseModel("Accepted.", "Media file will be updated into relevant bug.", status.HTTP_202_ACCEPTED)


@router.get("/{id}", response_description="Bug data retrieved.")
async def get_bug(id):
    bug = await retrieve_bug(id)
    return ResponseModel(bug, "Bug data retrieved successfully") \
        if bug \
        else ErrorResponseModel("An error occured.", 404, "Bug doesn't exist.")
