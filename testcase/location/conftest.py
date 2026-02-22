# testcase/location/conftest.py
import os
import json
import pytest
from path import DATA

def load_data(env: str, key: str = None):
    """
    load location 專屬的測試資料。
    """
    json_file_path = os.path.join(DATA, env, "location.json")
    with open(json_file_path, 'r', encoding='utf-8') as f:
        test_data = json.load(f)
    
    if key:
        return test_data.get(key)
    return test_data

# --- 以下為提供給各個 Testcase 的專屬 Fixture ---

@pytest.fixture(scope="session")
def first_location_data():
    """提供給 test_get_first_location 使用 (單筆資料)"""
    return load_data("UAT", "get_first_location")

@pytest.fixture(scope="session")
def single_location_data():
    """提供給 test_get_earth 使用 (單筆資料)"""
    return load_data("UAT", "get_single_location")

@pytest.fixture(params=load_data("UAT", "filter_locations"), ids=lambda d: d["case_name"])
def filter_location_data(request):
    """參數化 Fixture: 提供給 test_filter_location_by_name 使用 (可擴充多筆)"""
    return request.param

@pytest.fixture(params=load_data("UAT", "multiple_locations"), ids=lambda d: d["case_name"])
def multiple_location_data(request):
    """參數化 Fixture: 取代原本寫死在 test_get_multiple_locations_by_id 的陣列"""
    return request.param