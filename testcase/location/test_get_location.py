import pytest
import logging
from schemas.common import PaginatedResponse
from schemas.location import LocationModel


def test_get_first_locations(location):
    """驗證所有地點中的第一個地點，並驗證其資料正確性"""
    response = location.get_all_locations()
    validated_data = PaginatedResponse[LocationModel](**response.json())
    first_location = validated_data.results[0]

    assert response.status_code == 200
    assert validated_data.info.count > 0
    assert validated_data.info.pages > 0
    assert first_location.id == 1
    assert first_location.name == "Earth (C-137)"
    assert first_location.type == "Planet"
    assert first_location.dimension == "Dimension C-137"


# 測試案例的程式碼現在變得非常乾淨，完全不需要關心 base_url 和 headers
# def test_get_earth(location):
#     """
#     測試取得 ID 為 1 的地點 (Earth C-137)
    
#     參數 'location' 由 conftest.py 中的 fixture 自動注入，
#     它是一個已經初始化好的 Location 物件。
#     """
#     # 直接使用已經初始化好的 api 物件
#     response = location.get_single_location(1)
#     assert response.status_code == 200
#     logging.info(f"API 回傳的完整資料: {response}")  # 新增這行來印出完整回應內容
#     # assert response.status_code == 200
#     # response_data = response.json()
#     assert response["name"] == "Earth (C-137)"
#     assert response["dimension"] == "Dimension C-137"


# def test_filter_location_by_name(location):
#     """
#     測試透過名稱篩選地點
#     """
#     response = location.filter_locations(name="Post-Apocalyptic Earth")
#     logging.info(f"API 回傳的完整資料: {type(response)}")  # 新增這行來印出完整回應內容
    # assert response.status_code == 200
    # response_data = response.json()
    
    # API 可能回傳多個結果，我們檢查第一筆
    # assert len(response_data["results"]) > 0
    # assert response_data["results"][0]["name"] == "Post-Apocalyptic Earth"
    # assert response_data["results"][0]["type"] == "Planet"

# @pytest.mark.parametrize("location_id, expected_name", [
#     (1, "Earth (C-137)"),
#     (2, "Abadango"),
#     (3, "Citadel of Ricks")
# ])
# def test_get_multiple_locations_by_id(location, location_id, expected_name):
#     """
#     使用參數化來測試多個地點 ID
#     """
#     response = location.get_single_location(location_id)
#     logging.info(f"API 回傳的完整資料: {response}")  # 新增這行來印出完整回應內容

    # assert response.status_code == 200
    # assert response.json()["name"] == expected_name

