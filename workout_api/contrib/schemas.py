from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador', example='a234-234234-234234')]
    created_at: Annotated[datetime, Field(description='Data de criação', example='2023-01-01 00:00:00')]