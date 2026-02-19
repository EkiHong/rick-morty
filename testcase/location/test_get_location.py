import pytest
import logging
from schemas.common import PaginatedResponse
from schemas.location import LocationModel


def test_get_first_location(location):
    """ 驗證以下資訊
        1. all location 的回傳資料型態
        2. 所有地點中的第一個地點的資料是否正確
    """
    response = location.get_all_locations()
    validated_data = response.validate(PaginatedResponse[LocationModel])
    first_location = validated_data.results[0]

    assert response.status_code == 200
    assert validated_data.info.count > 0
    assert validated_data.info.pages > 0
    assert first_location.id == 1
    assert first_location.name == "Earth (C-137)"
    assert first_location.type == "Planet"
    assert first_location.dimension == "Dimension C-137"


def test_get_earth(location):
    """
    驗證取得 ID 為 1 的地點 (Earth C-137)
    """
    response = location.get_single_location(1)
    validated_data = response.validate(LocationModel)
    
    assert response.status_code == 200
    assert validated_data.id == 1
    assert validated_data.name == "Earth (C-137)"
    assert validated_data.dimension == "Dimension C-137"


def test_filter_location_by_name(location):
    """
    測試透過名稱篩選地點
    """
    response = location.filter_locations(name="Post-Apocalyptic Earth")
    validated_data = response.validate(PaginatedResponse[LocationModel])
    
    assert response.status_code == 200
    assert len(validated_data.results) > 0
    assert validated_data.results[0].name == "Post-Apocalyptic Earth"
    assert validated_data.results[0].type == "Planet"


@pytest.mark.parametrize("location_id, expected_name", [
    (1, "Earth (C-137)"),
    (2, "Abadango"),
    (3, "Citadel of Ricks"), 
    (4, "Worldender's lair")
])
def test_get_multiple_locations_by_id(location, location_id, expected_name):
    """
    透過不同 ID 查詢不同地點，並驗證每個地點的資料是否正確。
    """
    response = location.get_single_location(location_id)
    validated_data = response.validate(LocationModel)

    assert response.status_code == 200
    assert len(validated_data.name) > 0
    assert validated_data.name == expected_name

