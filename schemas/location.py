from pydantic import HttpUrl
from schemas.base import APIResponseBase
from pydantic import BaseModel, ConfigDict
from typing import Optional

# 建立 Request 規則，可以在建立假測資時，請 Polygon 依照這個規則來產生資料，提供反向測案的測資結構定義
class LocationQueryParamsRequestModel(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    dimension: Optional[str] = None


class LocationResponseModel(APIResponseBase):
    id: int
    name: str
    type: str
    dimension: str
    residents: list[HttpUrl]
    url: HttpUrl
    created: str
