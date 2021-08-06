
from fastapi import APIRouter, status, Body
from fastapi.encoders import jsonable_encoder

from app.models.common import *
from app.models.brand import *
from app.database.crud.brand import *
from app.database.crud.bug import retrive_bugs_of_brand
from app.database.crud.app import retrive_apps_of_brand


router = APIRouter()


@router.get('/', response_description="Brands are retrieved.")
async def get_brands():
    brands = await retrieve_brands()
    return ResponseModel(brands, "Brands data retrieved successfully") \
        if len(brands) > 0 \
        else ResponseModel(
        brands, "Empty list returned"
    )


@router.post('/', response_description="Brands data added into the database.")
async def add_brand(brand: BrandModel = Body(...)):
    brand = jsonable_encoder(brand)
    new_brand = await add_new_brand(brand)
    return ResponseModel(new_brand, "Brand created successfully.", status.HTTP_201_CREATED)


@router.get('/get-api-key', response_description="Api key for brand generated successfully")
async def generate_api_key(id: str):
    #generated_api_key = generate_auth_key()
    brand = await update_brand_api_key(id)
    return brand


@router.get("/{id}", response_description="Brand data retrieved.")
async def get_brand(id):
    brand = await retrieve_brand(id)
    return ResponseModel(brand, "Brand data retrieved successfully") \
        if brand \
        else ErrorResponseModel("An error occured.", 404, "Brand doesn't exist.")


@router.put('/{id}', response_description="User data updated in the database.")
async def update_brand(id: str, brand: UpdateBrandModel = Body(...)):
    brand = jsonable_encoder(brand)
    updated_brand = await update_brand_data(id, brand)
    return ResponseModel({"id": id},
                         "User updated successfully") \
        if updated_brand \
        else ErrorResponseModel("An error occurred", status.HTTP_404_NOT_FOUND, "There was an error updating the brand.")


@router.get("/{id}/apps", response_description="Apps retrieved for brand.")
async def get_apps_of_a_brand(id):
    apps = await retrive_apps_of_brand(id)
    return ResponseModel(apps, "Brand data retrieved successfully") \
        if apps \
        else ErrorResponseModel("An error occured.", 404, "Brand doesn't exist.")


@router.get("/{id}/bugs", response_description="Bugs retrieved from brand.")
async def get_bugs_of_brand(id):
    bugs = await retrive_bugs_of_brand(id)
    return ResponseModel(bugs, "Brand data retrieved successfully") \
        if bugs \
        else ErrorResponseModel("An error occured.", 404, "Brand doesn't exist.")
