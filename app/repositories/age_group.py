from typing import List, Optional

from bson import ObjectId
from pydantic import TypeAdapter
from pymongo.synchronous.database import Database

from app.schemas.age_group import AgeGroupRead, AgeGroupCreate
from app.schemas.filters import AgeGroupFilter


class AgeGroupRepository:
    def __init__(self, db: Database):
        self.collection = db.age_groups

    def create(self, age_group_payload: AgeGroupCreate) -> AgeGroupRead:
        age_group_data = age_group_payload.model_dump()

        age_group = self.collection.insert_one(age_group_data)

        return AgeGroupRead(id=str(age_group.inserted_id), **age_group_data)

    def get(self, age_group_id: str) -> Optional[AgeGroupRead]:
        age_group = self.collection.find_one({"_id": ObjectId(age_group_id)})

        if not age_group:
            return None

        return AgeGroupRead(**age_group)

    def list(self, filter_query: AgeGroupFilter = None) -> List[AgeGroupRead]:
        filters = None
        if filter_query:
            if filter_query.age is not None:
                filters = {
                    "$and": [
                        {"minimum_age": {"$lte": filter_query.age}},
                        {"maximum_age": {"$gte": filter_query.age}},
                    ]
                }

        age_groups = self.collection.find(filter=filters)
        return TypeAdapter(List[AgeGroupRead]).validate_python(age_groups)

    def delete(self, age_group_id: str) -> bool:
        age_group = self.collection.find_one_and_delete({"_id": ObjectId(age_group_id)})
        return bool(age_group)
