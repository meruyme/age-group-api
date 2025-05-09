from typing import Optional
from pydantic import BaseModel

from app.fields import Age


class AgeGroupFilter(BaseModel):
    maximum_age: Optional[Age] = None
    minimum_age: Optional[Age] = None
