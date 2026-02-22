from schemas.common import PaginatedResponse
from schemas.location import LocationResponseModel

def test_get_first_location(location, first_location_data):
    """ 驗證所有地點中的第一個地點的資料是否與預期相符 """
    response = location.get_all_locations()
    validated_data = response.validate(PaginatedResponse[LocationResponseModel])
    first_loc = validated_data.results[0]

    assert response.status_code == first_location_data["expected_status"]
    assert validated_data.info.count > 0
    assert validated_data.info.pages > 0
    assert first_loc.id == first_location_data["expected_id"]
    assert first_loc.name == first_location_data["expected_name"]
    assert first_loc.type == first_location_data["expected_type"]
    assert first_loc.dimension == first_location_data["expected_dimension"]


def test_get_earth(location, single_location_data):
    """ 驗證取得特定 ID 的地點 """
    response = location.get_single_location(single_location_data["location_id"])
    validated_data = response.validate(LocationResponseModel)
    
    assert response.status_code == single_location_data["expected_status"]
    assert validated_data.id == single_location_data["location_id"]
    assert validated_data.name == single_location_data["expected_name"]
    assert validated_data.dimension == single_location_data["expected_dimension"]


def test_filter_location_by_name(location, filter_location_data):
    """ 測試透過參數篩選地點 (支援動態多組參數) """
    # ** 字典解包，將 JSON 裡的 query_params 自動轉成函式參數
    response = location.filter_locations(**filter_location_data["query_params"])
    validated_data = response.validate(PaginatedResponse[LocationResponseModel])
    
    assert response.status_code == filter_location_data["expected_status"]
    assert len(validated_data.results) > 0
    assert validated_data.results[0].name == filter_location_data["expected_name"]
    assert validated_data.results[0].type == filter_location_data["expected_type"]


def test_get_multiple_locations_by_id(location, multiple_locations_data):
    """ 透過不同 ID 查詢不同地點，驗證回傳結果 """
    response = location.get_single_location(multiple_locations_data["location_id"])
    validated_data = response.validate(LocationResponseModel)

    assert response.status_code == multiple_locations_data["expected_status"]
    assert len(validated_data.name) > 0
    assert validated_data.name == multiple_locations_data["expected_name"]