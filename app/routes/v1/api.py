from fastapi import APIRouter, Depends

from .endpoints import users, brands, apps, bugs, slack, clickup
from app.middlewares.auth.jwt_bearer import JWTBearer

token_listener = JWTBearer()
router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(
    brands.router,
    prefix="/brands",
    tags=["Brands"],
    dependencies=[Depends(token_listener)],
)
router.include_router(
    apps.router, prefix="/apps", tags=["Apps"], dependencies=[Depends(token_listener)]
)
router.include_router(
    bugs.router, prefix="/bugs", tags=["Bugs"], dependencies=[Depends(token_listener)]
)
router.include_router(
    slack.router,
    prefix="/slack-integration",
    tags=["Slack Integration"],
    dependencies=[Depends(token_listener)],
)
router.include_router(
    clickup.router,
    prefix="/clickup-integration",
    tags=["Clickup Integration"],
    dependencies=[Depends(token_listener)],
)
