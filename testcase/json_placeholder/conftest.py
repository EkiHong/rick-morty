import pytest
from utils.common import load_test_data


@pytest.fixture(
    params=load_test_data("json_placeholder", "test_create_new_article"), 
    ids=lambda d: d["case_name"]
)
def create_article_data(request):
    """提供給正向新增文章測試的參數化 Fixture"""
    return request.param

@pytest.fixture(
    params=load_test_data("json_placeholder", "test_update_article"), 
    ids=lambda d: d["case_name"]
)
def update_article_data(request):
    """提供給更新文章測試的參數化 Fixture"""
    return request.param

@pytest.fixture(
    params=load_test_data("json_placeholder", "test_create_article_negative"), 
    ids=lambda d: d["case_name"]
)
def negative_data(request):
    return request.param