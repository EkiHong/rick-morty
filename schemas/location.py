from pydantic import HttpUrl
from schemas.base import APIResponseBase


class LocationResponseModel(APIResponseBase):
    id: int
    name: str
    type: str
    dimension: str
    # residents 是一個陣列，裡面裝的必須是合法的 URL 格式
    residents: list[HttpUrl]
    url: HttpUrl
    created: str
