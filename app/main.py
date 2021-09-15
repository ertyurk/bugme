from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routes.v1.api import router as api_router

app = FastAPI(
    title="BUGME",
    description="""
    A Bug orchestration tool for mobile applications.
    In this application, you can create Users, Brands, Apps and report bugs and add Slack, Clickup integrations.
    Users can have multiple Brands (Users can be considered as Organizations too)
    Brands can have multiple Apps
    For bug reporting, you need to use api key generated from brand (The Api key will be generated when you add a new brand automatically but also, you can generate a new one via {API_URL}/api/v1/brands/get-api-key with Brand ID param)
    Client apps can report bugs along with Bundle ID and Platform and other details can be found in {API_URL}/docs. If the bundle ID is not saved, We create a new APP for that bundle ID along with correspondent Brand ID and User ID and platform information.
    """,
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
