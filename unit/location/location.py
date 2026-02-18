from typing import List, Optional

# 我們假設 RequestAPI 類別存在於 framework.request_api 模組中
# 並且提供了 self.get() 方法來發送 HTTP GET 請求。
from framework.request_api import RequestAPI


class Location(RequestAPI):
    """
    用於 /location 端點的 API 客戶端。
    繼承自 RequestAPI 以處理底層 HTTP 請求。
    """

    def __init__(self, base_url: str):
        """
        初始化 Location。
        :param base_url: API 的基礎 URL (例如: https://rickandmortyapi.com/api)
        """
        super().__init__(base_url)
        self.path_prefix = "/location"
        self.set_api()  # 呼叫 set_api 來設定此業務邏輯層的 API 細節
        self.url  = None

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
        注意：API 文件中的 'type' 是 Python 的保留關鍵字，
        因此在函式參數中我們使用 'location_type' 來避免衝突。
        對應於: GET /location?name=...&type=...&dimension=...
        """
        params = {
            "name": name,
            "type": location_type,
            "dimension": dimension
        }
        # 過濾掉值為 None 的參數，以建立乾淨的查詢
        cleaned_params = {k: v for k, v in params.items() if v is not None}
        return self.get(self.path_prefix, params=cleaned_params)

