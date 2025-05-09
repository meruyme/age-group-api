from fastapi import Depends
from pymongo.synchronous.database import Database

from app.core.db import DatabaseProvider
from app.repositories.age_group import AgeGroupRepository
from app.services.age_group import AgeGroupService


def get_database() -> Database:
    return DatabaseProvider.get_database()


def get_age_group_repository(db: Database = Depends(get_database)) -> AgeGroupRepository:
    return AgeGroupRepository(db)


def get_age_group_service(
    age_group_repository: AgeGroupRepository = Depends(get_age_group_repository)
) -> AgeGroupService:
    return AgeGroupService(age_group_repository)
