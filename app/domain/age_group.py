from typing import Optional, Iterator, List

from bson import ObjectId
from fastapi.exceptions import HTTPException
from fastapi import status
from pydantic import parse_obj_as
from pymongo.synchronous.database import Database

from app.schemas.age_group import AgeGroupRead, AgeGroupCreate
from app.schemas.filters import AgeGroupFilter


class AgeGroupDomain:
    def __init__(self, db: Database):
        self.collection = db.age_groups

    def create(self, age_group_payload: AgeGroupCreate) -> AgeGroupRead:
        if self.__is_duplicated_age_group(age_group_payload):
            raise HTTPException(
                detail="Age group already exists.", status_code=status.HTTP_400_BAD_REQUEST,
            )

        age_group_data = age_group_payload.model_dump()

        age_group = self.collection.insert_one(age_group_data)

        return AgeGroupRead(id=str(age_group.inserted_id), **age_group_data)

    def get(self, age_group_id: str) -> AgeGroupRead:
        age_group = self.collection.find_one({"_id": ObjectId(age_group_id)})

        if not age_group:
            raise HTTPException(
                detail="Age group not found.", status_code=status.HTTP_404_NOT_FOUND,
            )

        return AgeGroupRead(**age_group)

    def list(self, filter_query: AgeGroupFilter = None) -> List[AgeGroupRead]:
        filters = None
        if filter_query:
            filters = filter_query.model_dump(exclude_none=True) or None

        age_groups = self.collection.find(filter=filters)
        return parse_obj_as(List[AgeGroupRead], age_groups)

    def delete(self, age_group_id: str):
        self.collection.find_one_and_delete({"_id": ObjectId(age_group_id)})

    def __is_duplicated_age_group(self, age_group_payload: AgeGroupCreate) -> bool:
        all_age_groups = self.list()
        for age_group in all_age_groups:
            if (
                age_group.minimum_age == age_group_payload.minimum_age and
                age_group.maximum_age == age_group_payload.maximum_age
            ):
                return True
        return False
