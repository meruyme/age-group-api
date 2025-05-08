from pydantic import BaseModel, Field, model_validator

from app.fields import PyObjectId


class AgeGroupBase(BaseModel):
    maximum_age: int = Field(ge=0, lt=150)
    minimum_age: int = Field(ge=0, lt=150)


class AgeGroupCreate(AgeGroupBase):

    @model_validator(mode="after")
    def is_age_group_valid(self):
        if self.minimum_age > self.maximum_age:
            raise ValueError("Minimum age must be lower than maximum age.")
        return self


class AgeGroupRead(AgeGroupBase):
    id: PyObjectId = Field(alias="_id")
