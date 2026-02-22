import pytest
from utils.common import load_test_data

@pytest.fixture(scope="session")
def first_location_data():
    """提供給 test_get_first_location 使用 (單筆資料)"""
    return load_test_data("location", "test_get_first_location")

@pytest.fixture(scope="session")
def single_location_data():
    """提供給 test_get_earth 使用 (單筆資料)"""
    return load_test_data("location", "test_get_earth")

@pytest.fixture(params=load_test_data("location", "test_filter_location_by_name"), ids=lambda d: d["case_name"])
def filter_location_data(request):
    """參數化 Fixture: 提供給 test_filter_location_by_name 使用 (動態多筆)"""
    return request.param

@pytest.fixture(params=load_test_data("location", "test_get_multiple_locations_by_id"), ids=lambda d: d["case_name"])
def multiple_locations_data(request):
    """參數化 Fixture: 提供給 test_get_multiple_locations_by_id 使用 (動態多筆)"""
    return request.param