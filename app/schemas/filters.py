from typing import Optional
from pydantic import BaseModel, Field


class AgeGroupFilter(BaseModel):
    maximum_age: Optional[int] = Field(ge=0, lt=150, default=None)
    minimum_age: Optional[int] = Field(ge=0, lt=150, default=None)
