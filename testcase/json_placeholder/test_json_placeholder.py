import pytest
from schemas.json_placeholder import JsonPlaceholderRequestModel, JsonPlaceholderResponseModel
from utils.common import deep_update
from utils.factories.fakedata_factory import JsonPlaceholderFactory


def test_create_new_article(json_placeholder_api):
    """
    驗證 POST
    """
    # 1. 準備 Payload (由 Pydantic 嚴格確保您不會少傳欄位或傳錯型別)
    request_data = JsonPlaceholderRequestModel(
        title="Testing Framework POST",
        body="It works perfectly!",
        userId=99
    )

    # 2. 呼叫業務層 API (利用 .model_dump() 將 Pydantic 物件轉成字典送出)
    response = json_placeholder_api.create_article(payload=request_data.model_dump())

    # 3. 驗證 HTTP 狀態碼 (這證明了我們底層 APIResponse 封裝得很好)
    assert response.status_code == 201
    
    # 4. 驗證 Response 結構與內容
    validated_data = response.validate(JsonPlaceholderResponseModel)
    
    assert validated_data.id > 0
    assert validated_data.title == request_data.title
    assert validated_data.body == request_data.body
    assert validated_data.userId == request_data.userId

def test_update_article(json_placeholder_api):
    """
    驗證 PUT
    """
    request_data = JsonPlaceholderRequestModel(
        title="Updated Title",
        body="Updated Body",
        userId=99
    )

    # 更新 ID 為 1 的貼文
    response = json_placeholder_api.update_article(article_id=1, payload=request_data.model_dump())
    
    assert response.status_code == 200
    validated_data = response.validate(JsonPlaceholderResponseModel)
    assert validated_data.title == "Updated Title"

def test_create_article_negative(json_placeholder_api, negative_data):
    """
    負向測試：使用 JsonPlaceholderFactory 動態生成基底，再用 JSON 資料覆蓋測試邊界值
    """
    
    # 1. 取得絕對合法的基底 (Base Payload)
    # JsonPlaceholderFactory.build() 會產出一個完整的 Pydantic 物件
    # 我們馬上呼叫 .model_dump() 將它轉為純 Python Dictionary
    base_payload = JsonPlaceholderFactory.build().model_dump()
    
    # 2. 深度合併變異資料 (把 title 換成 null 或空字串)
    update_payload = deep_update(base_payload, negative_data["override"])
    
    # 3. 發送請求給 API 伺服器
    response = json_placeholder_api.create_article(payload=update_payload)
    
    # 4. 驗證伺服器是否如期擋下錯誤資料
    assert response.status_code == negative_data["expected_status"]