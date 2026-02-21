import pytest
from unit import Location

from env.all import get_env_config


@pytest.fixture(scope="session")
def location():
    """
    這個 fixture 會建立並回傳一個已經設定好 base_url 和 headers 的 Location 物件。
    scope="session" 表示在整個測試會話中，這個 fixture 只會執行一次。
    """
    # 1. 從環境配置中讀取固定不變的值
    config = get_env_config()
    base_url = config.get('base_url')
    # headers = config.get('headers')

    # 2. 實例化業務邏輯層的 API Client
    api = Location(base_url=base_url)

    # 3. 將初始化好的物件提供給測試案例
    yield api


import pytest
from unit import Location
from unit.json_placeholder.json_placeholder import JSONPlaceholder


# get_config() 之後必須修改成給予對應的參數(UAT, STG)，讓他去讀對應的 json 檔案，
# 例如讀取 common.json 或是 json_placeholder.json，這樣才能拿到對應的 base_url 及 對應的測資。
@pytest.fixture(scope="session")
def json_placeholder_api():
    """
    專門提供給 JSONPlaceholder 測試使用的 API Client Fixture。
    它的 base_url 是獨立的，與環境變數中的 Rick & Morty 無關。
    """

    base_url = "https://jsonplaceholder.typicode.com"
    api = JSONPlaceholder(base_url=base_url)
    yield api
