from pydantic import BaseModel, model_validator

from app.fields import PyObjectId, Age


class AgeGroupBase(BaseModel):
    maximum_age: Age
    minimum_age: Age


class AgeGroupCreate(AgeGroupBase):

    @model_validator(mode="after")
    def is_age_group_valid(self):
        if self.minimum_age > self.maximum_age:
            raise ValueError("Minimum age must be lower than maximum age.")
        return self


class AgeGroupRead(AgeGroupBase):
    id: PyObjectId
