from typing import Optional
from pydantic import BaseModel

from app.fields import Age


class AgeGroupFilter(BaseModel):
    age: Optional[Age] = None
