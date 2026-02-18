from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class AbstractAPI(ABC):
    """API 抽象類別"""

    def __init__(self):
        self.base_url = None
        self.headers = {}
        self.timeout = 30
        self.response = None
        self.status_code = None
   

    @abstractmethod
    def set_api(self):
        """API 基本資訊"""
        raise NotImplementedError("子類別必須實作 set_api 方法")


    @abstractmethod
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """GET 請求"""
        pass

    @abstractmethod
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """POST 請求"""
        pass

    @abstractmethod
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """PUT 請求"""
        pass

    @abstractmethod
    def delete(self, endpoint: str) -> Dict:
        """DELETE 請求"""
        pass
