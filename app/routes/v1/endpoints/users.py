from fastapi.exceptions import HTTPException

from fastapi import APIRouter, status, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials

from app.models.common import *
from app.models.user import *
from app.database.crud.user import *
from app.database.crud.brand import retrive_brands_of_user
from app.middlewares.auth.jwt_bearer import JWTBearer
from app.database.crud.app import retrive_apps_of_user

router = APIRouter()
token_listener = JWTBearer()


@router.post("/login/")
async def login(credentials: HTTPBasicCredentials = Body(...)):
    user = await user_login(jsonable_encoder(credentials))
    if user == False:
        return ErrorResponseModel(
            "An error occurred",
            status.HTTP_403_FORBIDDEN,
            "Incorrect email or password.",
        )
    return ResponseModel(user, "Successfully logged in!")


@router.post("/register/", response_description="Account created.")
async def user_registration(user: UserModel = Body(...)):
    new_user = await create_user(jsonable_encoder(user))
    if new_user == False:
        return ErrorResponseModel(
            "An error occurred", status.HTTP_409_CONFLICT, "Email already in use."
        )
    return ResponseModel(new_user, "User created successfully")


@router.get(
    "/",
    dependencies=[Depends(token_listener)],
    response_description="Users are retrieved.",
)
async def get_users():
    users = await retrieve_users()
    return (
        ResponseModel(users, "Users data retrieved successfully")
        if len(users) > 0
        else ResponseModel(users, "Empty list returned")
    )


@router.get(
    "/{id}/",
    dependencies=[Depends(token_listener)],
    response_description="User data retrieved.",
)
async def get_user(id):
    user = await retrieve_user(id)
    return (
        ResponseModel(user, "User data retrieved successfully")
        if user
        else ErrorResponseModel("An error occured.", 404, "Student doesn't exist.")
    )


@router.put(
    "/{id}/",
    dependencies=[Depends(token_listener)],
    response_description="User data updated in the database.",
)
async def update_user(id: str, user: UpdateUserModel = Body(...)):
    user = jsonable_encoder(user)
    updated_user = await update_user_data(id, user)
    return (
        ResponseModel({"id": id}, "User updated successfully")
        if updated_user
        else ErrorResponseModel(
            "An error occurred",
            status.HTTP_404_NOT_FOUND,
            f"There was an error updating the user {id}",
        )
    )


@router.get(
    "/{id}/brands/",
    dependencies=[Depends(token_listener)],
    response_description="User brands are retrieved.",
)
async def get_brands_of_users(id):
    brands = await retrive_brands_of_user(id)
    return (
        ResponseModel(brands, "User brands are successfully")
        if brands
        else ErrorResponseModel("An error occured.", 404, "Student doesn't exist.")
    )


@router.get(
    "/{id}/apps/",
    dependencies=[Depends(token_listener)],
    response_description="User brands are retrieved.",
)
async def get_apps_of_user(id):
    apps = await retrive_apps_of_user(id)
    return (
        ResponseModel(apps, "User brands are successfully")
        if apps
        else ErrorResponseModel("An error occured.", 404, "Student doesn't exist.")
    )
