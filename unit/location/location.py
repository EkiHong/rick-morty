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

    def filter_locations(self,
                         name: Optional[str] = None,
                         location_type: Optional[str] = None,
                         dimension: Optional[str] = None):
        """
        根據查詢參數篩選地點。
        注意: API 文件中的 'type' 是 Python 的保留關鍵字，
        GET /location?name=...&type=...&dimension=...
        """
        params = {
            "name": name,
            "type": location_type,
            "dimension": dimension
        }
        # 過濾掉值為 None 的參數，以建立乾淨的查詢
        cleaned_params = {k: v for k, v in params.items() if v is not None}
        return self.get(self.path_prefix, params=cleaned_params)

