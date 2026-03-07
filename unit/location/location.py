from typing import List, Optional
from framework.request_api import RequestAPI


class Location(RequestAPI):

    def __init__(self, base_url: str):
        """
        初始化 Location。
        :param base_url: API 的基礎 URL (https://rickandmortyapi.com/api)
        """
        super().__init__(base_url)
        self.path_prefix = "/location"
        self.set_api()  # 呼叫 set_api 來設定此業務邏輯層的 API 細節

    def set_api(self):
        """設定 Location API 的特有資訊"""
        self.url = self.base_url + self.path_prefix
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_single_location(self, location_id: int):
        """
        透過 ID 獲取單一地點的資訊。
        對應於: GET /location/{id}
        """
        path = f"{self.path_prefix}/{location_id}"
        return self.get(path)

    def get_multiple_locations(self, location_ids: List[int]):
        """
        透過 ID 列表獲取多個地點的資訊。
        對應於: GET /location/{id1},{id2},...
        """
        # 將整數列表轉換為逗號分隔的字串
        ids_str = ",".join(map(str, location_ids))
        path = f"{self.path_prefix}/{ids_str}"
        return self.get(path)

    def get_all_locations(self, page: Optional[int] = None):
        """
        獲取所有地點的資訊，可選分頁。
        對應於: GET /location 或 GET /location?page={page}
        """
        params = {}
        if page:
            params["page"] = page
        return self.get(self.path_prefix, params=params)


    def filter_locations(self, **kwargs):
            """
            Point of Extension: 這裡我們使用 **kwargs 來實現更靈活的參數接收。
            透過 **kwargs 動態接收所有查詢參數。
            Testcase 傳入 {"name": "Earth", "type": None}，
            這裡的 kwargs 就會是 {"name": "Earth", "type": None}
            這裡完全不使用 Pydantic 檢查，直接接收 Testcase 傳來的任何變異資料 (包含型別錯誤)，
            並原封不動地交給 Framework 底層。底層只會負責過濾掉 None。
            """
            return self.get(self.path_prefix, params=kwargs)
