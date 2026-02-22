import pytest
from schemas.json_placeholder import JsonPlaceholderRequestModel, JsonPlaceholderResponseModel
from utils.common import deep_update
from utils.factories.fakedata_factory import JsonPlaceholderFactory


def test_create_new_article(json_placeholder_api, create_article_data):
    """正向測試：驗證 POST 功能是否能成功建立資料"""
    # 1. 取得 Factory 合法基底，並混入 JSON 測資的覆寫設定
    base_payload = JsonPlaceholderFactory.build().model_dump()
    final_payload = deep_update(base_payload, create_article_data.get("payload_override", {}))
    
    # 2. 發送請求
    response = json_placeholder_api.create_article(payload=final_payload)
    assert response.status_code == create_article_data["expected_status"]
    
    # 3. 如果預期成功，驗證回傳資料與送出的 final_payload 是否完全一致
    if create_article_data["expected_status"] == 201:
        validated_data = response.validate(JsonPlaceholderResponseModel)
        assert validated_data.id > 0
        assert validated_data.title == final_payload["title"]
        assert validated_data.body == final_payload["body"]
        assert validated_data.userId == final_payload["userId"]

def test_update_article(json_placeholder_api, update_article_data):
    """正向測試：驗證 PUT 功能是否能成功更新資料"""
    base_payload = JsonPlaceholderFactory.build().model_dump()
    final_payload = deep_update(base_payload, update_article_data.get("payload_override", {}))
    
    # 從 JSON 測資中動態取得要更新的目標 ID
    target_id = update_article_data["article_id"]
    response = json_placeholder_api.update_article(article_id=target_id, payload=final_payload)
    
    assert response.status_code == update_article_data["expected_status"]
    
    if update_article_data["expected_status"] == 200:
        validated_data = response.validate(JsonPlaceholderResponseModel)
        assert validated_data.id == target_id
        assert validated_data.title == final_payload["title"]
        assert validated_data.body == final_payload["body"]
        assert validated_data.userId == final_payload["userId"]


def test_create_article_negative(json_placeholder_api, negative_data):
    """
    負向測試：使用 Polyfactory 動態生成基底，再用 JSON 資料覆蓋測試邊界值
    """
    
    # 1. 取得絕對合法的基底 (Base Payload)
    # JsonPlaceholderFactory.build() 會產出一個完整的 Pydantic 物件
    # 我們馬上呼叫 .model_dump() 將它轉為純 Python Dictionary
    base_payload = JsonPlaceholderFactory.build().model_dump()

    # 2. 深度合併變異資料 (直接使用 JSON 裡的 Key: "payload_override")
    final_payload = deep_update(base_payload, negative_data["payload_override"])
    
    # 3. 發送請求給 API 伺服器
    response = json_placeholder_api.create_article(payload=final_payload)
    
    # 4. 驗證伺服器是否如期擋下錯誤資料
    assert response.status_code == negative_data["expected_status"]