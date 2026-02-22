from typing import Dict
from framework.request_api import RequestAPI

class JSONPlaceholder(RequestAPI):

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.path_prefix = "/posts"
        self.set_api()

    def set_api(self):
        self.url = self.base_url + self.path_prefix
        self.headers = {
            "Content-type": "application/json; charset=UTF-8",
        }

    def create_article(self, payload: Dict):
        """
        業務邏輯：新增貼文
        """
        return self.post(self.path_prefix, json=payload)

    def update_article(self, article_id: int, payload: Dict):
        """
        業務邏輯：修改貼文
        """
        return self.put(self.path_prefix + f"/{article_id}", json=payload)