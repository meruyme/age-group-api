from fastapi import APIRouter

from app.routers.v1 import age_group

router = APIRouter(prefix="/v1")
router.include_router(age_group.router)
