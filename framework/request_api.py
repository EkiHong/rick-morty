import requests
from typing import Dict, Any
from framework.abstract_api import AbstractAPI
from framework.response_wrapper import APIResponse

class RequestAPI(AbstractAPI):
    """使用 requests 套件實作的 API 類別"""

    def __init__(self, base_url: str = ""):
        super().__init__()
        self.base_url = base_url  
        self.session = requests.Session()

    def set_api(self):
        pass

    def get(self, endpoint: str, **kwargs) -> APIResponse:
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("headers", self.headers)
        kwargs.setdefault("timeout", self.timeout)

        try:
            response = self.session.get(url, **kwargs)
            return APIResponse(response)

        except Exception as e:
            print(f"GET 請求失敗: {e}")
            return None

    def post(self, endpoint: str, **kwargs) -> APIResponse:
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("headers", self.headers)
        kwargs.setdefault("timeout", self.timeout)

        try:
            response = self.session.post(url, **kwargs)
            return APIResponse(response)

        except Exception as e:
            print(f"POST 請求失敗: {e}")
            return None

    def put(self, endpoint: str, **kwargs) -> APIResponse:
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("headers", self.headers)
        kwargs.setdefault("timeout", self.timeout)

        try:
            response = self.session.put(url, **kwargs)
            return APIResponse(response)

        except Exception as e:
            print(f"PUT 請求失敗: {e}")
            return None

        except Exception as e:
            print(f"PUT 請求失敗: {e}")
            return {}

    def delete(self, endpoint: str, **kwargs) -> Any:
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("headers", self.headers)
        kwargs.setdefault("timeout", self.timeout)

        try:
            response = self.session.delete(url, **kwargs)
            return APIResponse(response)

        except Exception as e:
            print(f"DELETE 請求失敗: {e}")
            return None
