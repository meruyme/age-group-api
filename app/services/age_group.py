from typing import List

from fastapi import HTTPException, status

from app.repositories.age_group import AgeGroupRepository
from app.schemas.age_group import AgeGroupCreate, AgeGroupRead
from app.schemas.filters import AgeGroupFilter


class AgeGroupService:
    def __init__(self, age_group_repository: AgeGroupRepository):
        self.repository = age_group_repository

    def create(self, age_group_payload: AgeGroupCreate) -> AgeGroupRead:
        if self.__is_duplicated_age_group(age_group_payload):
            raise HTTPException(
                detail="Age group already exists.", status_code=status.HTTP_400_BAD_REQUEST,
            )

        return self.repository.create(age_group_payload)

    def get(self, age_group_id: str) -> AgeGroupRead:
        age_group = self.repository.get(age_group_id)

        if not age_group:
            raise HTTPException(
                detail="Age group not found.", status_code=status.HTTP_404_NOT_FOUND,
            )

        return age_group

    def list(self, filter_query: AgeGroupFilter) -> List[AgeGroupRead]:
        return self.repository.list(filter_query)

    def delete(self, age_group_id: str):
        is_deleted = self.repository.delete(age_group_id)

        if not is_deleted:
            raise HTTPException(
                detail="Age group not found.", status_code=status.HTTP_404_NOT_FOUND,
            )

    def __is_duplicated_age_group(self, age_group_payload: AgeGroupCreate) -> bool:
        all_age_groups = self.repository.list()
        for age_group in all_age_groups:
            if (
                age_group.minimum_age == age_group_payload.minimum_age and
                age_group.maximum_age == age_group_payload.maximum_age
            ):
                return True
        return False
