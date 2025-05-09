from typing import Annotated

from pydantic import BeforeValidator, Field

PyObjectId = Annotated[str, Field(alias="_id"), BeforeValidator(str)]

Age = Annotated[int, Field(ge=0, lt=150)]
