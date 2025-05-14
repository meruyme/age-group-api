from typing import List, Annotated

from fastapi import APIRouter, Depends, status, Query

from app.dependencies import get_age_group_service
from app.schemas.age_group import AgeGroupRead, AgeGroupCreate
from app.schemas.filters import AgeGroupFilter
from app.services.age_group import AgeGroupService
from app.auth import get_current_username

router = APIRouter(
    prefix="/age-groups",
    tags=["Age Group API V1"],
    dependencies=[Depends(get_current_username)]
)


@router.post(
    "/",
    response_model=AgeGroupRead,
    status_code=status.HTTP_201_CREATED,
)
def create_age_group(payload: AgeGroupCreate, service: AgeGroupService = Depends(get_age_group_service)):
    return service.create(payload)


@router.get(
    "/{age_group_id}/",
    response_model=AgeGroupRead,
    status_code=status.HTTP_200_OK,
)
def get_age_group(age_group_id: str, service: AgeGroupService = Depends(get_age_group_service)):
    return service.get(age_group_id)


@router.get(
    "/",
    response_model=List[AgeGroupRead],
    status_code=status.HTTP_200_OK,
)
def list_age_group(
    filter_query: Annotated[AgeGroupFilter, Query()],
    service: AgeGroupService = Depends(get_age_group_service)
):
    return service.list(filter_query)


@router.delete(
    "/{age_group_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_age_group(age_group_id: str, service: AgeGroupService = Depends(get_age_group_service)):
    service.delete(age_group_id)
