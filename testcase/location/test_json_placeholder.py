import pytest
from schemas.json_placeholder import JsonPlaceholderRequestModel, JsonPlaceholderResponseModel

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