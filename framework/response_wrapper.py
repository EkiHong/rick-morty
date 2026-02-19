# framework/response_wrapper.py
import json
from requests import Response
from typing import TypeVar, Type

T = TypeVar('T')

class APIResponse:
    """封裝原始 HTTP Response，提供更安全的資料提取與 Pydantic 驗證"""
    def __init__(self, response: Response):
        self.raw_response = response
        self.status_code = response.status_code
        self.url = response.url
        self.headers = response.headers

    @property
    def json_data(self) -> dict:
        """安全地取得 JSON，如果不是 JSON 則回傳空字典"""
        try:
            return self.raw_response.json()
        except json.JSONDecodeError:
            return {}

    @property
    def text(self) -> str:
        return self.raw_response.text

    def validate(self, pydantic_model: Type[T]) -> T:
        """直接將回應轉化為 Pydantic 模型 (結合了我們之前討論的泛型)"""
        return pydantic_model(**self.json_data)