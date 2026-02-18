import pytest
from unit import Location

# 假設您有一個讀取環境配置的函式
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

