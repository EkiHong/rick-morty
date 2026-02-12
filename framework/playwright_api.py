from playwright.sync_api import sync_playwright, APIRequestContext, Playwright
from typing import Dict, Any, Optional
from framework.abstract_api import AbstractAPI


class PlaywrightAPI(AbstractAPI):
    """使用 Playwright 套件實作的 API 類別"""

    def __init__(self, base_url: str = ""):
        super().__init__()
        self.base_url = base_url
        self.playwright: Playwright = sync_playwright().start()
        self.context: APIRequestContext = self.playwright.request.new_context(
            base_url=self.base_url
        )

    def __del__(self):
        self.context.dispose()
        self.playwright.stop()

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """執行 GET 請求"""
        try:
            self.response = self.context.get(
                endpoint,
                params=params,
                headers=self.headers,
                timeout=self.timeout * 1000  # Playwright uses milliseconds
            )
            self.status_code = self.response.status
            return self.response.json()
        except Exception as e:
            print(f"GET 請求失敗: {e}")
            return {}

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """執行 POST 請求"""
        try:
            self.response = self.context.post(
                endpoint,
                data=data,
                headers=self.headers,
                timeout=self.timeout * 1000
            )
            self.status_code = self.response.status
            return self.response.json()
        except Exception as e:
            print(f"POST 請求失敗: {e}")
            return {}

    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """執行 PUT 請求"""
        try:
            self.response = self.context.put(
                endpoint,
                data=data,
                headers=self.headers,
                timeout=self.timeout * 1000
            )
            self.status_code = self.response.status
            return self.response.json()
        except Exception as e:
            print(f"PUT 請求失敗: {e}")
            return {}

    def delete(self, endpoint: str, **kwargs) -> Dict:
        """執行 DELETE 請求"""
        try:
            self.response = self.context.delete(
                endpoint,
                headers=self.headers,
                timeout=self.timeout * 1000
            )
            self.status_code = self.response.status
            if self.response.text():
                return self.response.json()
            return {"status": "success"}
        except Exception as e:
            print(f"DELETE 請求失敗: {e}")
            return {}
