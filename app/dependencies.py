from fastapi import Depends
from pymongo.synchronous.database import Database

from app.core.db import DatabaseProvider
from app.domain.age_group import AgeGroupDomain
from app.services.age_group import AgeGroupService


def get_database() -> Database:
    return DatabaseProvider.get_database()


def get_age_group_domain(db: Database = Depends(get_database)) -> AgeGroupDomain:
    return AgeGroupDomain(db)


def get_age_group_service(age_group_domain: AgeGroupDomain = Depends(get_age_group_domain)) -> AgeGroupService:
    return AgeGroupService(age_group_domain)
