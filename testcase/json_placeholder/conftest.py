# testcase/json_placeholder/conftest.py
import os
import json
import pytest
from path import DATA

def load_data(env, file_path: str = None) -> list:
    """
    負責讀取 json_placeholder 測試資料
    """
    # json_file_path = os.path.join(DATA, "UAT", "json_placeholder.json")
    json_file_path = os.path.join(DATA)
    with open(f"{json_file_path}/{env}/{file_path}", 'r', encoding='utf-8') as f:
        test_data = json.load(f)
    
    return [
        {
            "case_name": name, 
            "override": data["payload_override"], 
            "expected_status": data["expected_status"]
        }
        for name, data in test_data.items()
    ]

@pytest.fixture(params=load_data("UAT", "json_placeholder.json"), ids=lambda d: d["case_name"])
def negative_data(request):
    """
    區域性 Fixture：只對 testcase/json_placeholder/ 底下的測試有效
    """
    return request.param