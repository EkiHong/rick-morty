from pydantic import BaseModel, Field
from schemas.base import APIResponseBase

class JsonPlaceholderRequestModel(BaseModel):
    title: str
    body: str
    userId: int


class JsonPlaceholderResponseModel(APIResponseBase):
    id: int
    title: str
    body: str
    userId: int