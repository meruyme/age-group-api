from typing import List

from app.domain.age_group import AgeGroupDomain
from app.schemas.age_group import AgeGroupCreate, AgeGroupRead
from app.schemas.filters import AgeGroupFilter


class AgeGroupService:
    def __init__(self, age_group_domain: AgeGroupDomain):
        self.domain = age_group_domain

    def create(self, age_group_payload: AgeGroupCreate) -> AgeGroupRead:
        return self.domain.create(age_group_payload)

    def get(self, age_group_id: str) -> AgeGroupRead:
        return self.domain.get(age_group_id)

    def list(self, filter_query: AgeGroupFilter) -> List[AgeGroupRead]:
        return self.domain.list(filter_query)

    def delete(self, age_group_id: str):
        return self.domain.delete(age_group_id)
