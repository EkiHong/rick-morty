import requests
from typing import Dict, Any, Optional
from framework.abstract_api import AbstractAPI
import json


class RequestAPI(AbstractAPI):
    """使用 requests 套件實作的 API 類別"""

    def __init__(self, base_url: str = ""):
        super().__init__()
        self.base_url = base_url  # 往外丟是為了讓子類自己去決定 url
        self.session = requests.Session()
        # self.base_url = config.get("API_BASE_URL", "")
        # self.headers = config.get("API_HEADERS", {})
        # self.timeout = config.get("API_TIMEOUT", 30)

    def set_api(self):
        """設定 Request API 基本資訊"""
        pass

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """執行 GET 請求"""
        try:
            self.response = self.session.get(
                url=f"{self.base_url}{endpoint}",
                params=params,
                headers=self.headers,
                timeout=self.timeout
            )
            return self.response
            # self.status_code = self.response.status_code
            # return self.response.json()
        except Exception as e:
            print(f"GET 請求失敗: {e}")
            return {}

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """執行 POST 請求"""
        url = f"{self.base_url}{endpoint}"

        try:
            self.response = self.session.post(
                url,
                json=data,
                headers=self.headers,
                timeout=self.timeout
            )
            self.status_code = self.response.status_code
            return self.response.json()
        except Exception as e:
            print(f"POST 請求失敗: {e}")
            return {}

    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """執行 PUT 請求"""
        url = f"{self.base_url}{endpoint}"

        try:
            self.response = self.session.put(
                url,
                json=data,
                headers=self.headers,
                timeout=self.timeout
            )
            self.status_code = self.response.status_code
            return self.response.json()
        except Exception as e:
            print(f"PUT 請求失敗: {e}")
            return {}

    def delete(self, endpoint: str) -> Dict:
        """執行 DELETE 請求"""
        url = f"{self.base_url}{endpoint}"

        try:
            self.response = self.session.delete(
                url,
                headers=self.headers,
                timeout=self.timeout
            )
            self.status_code = self.response.status_code
            if self.response.text:
                return self.response.json()
            return {"status": "success"}
        except Exception as e:
            print(f"DELETE 請求失敗: {e}")
            return {}