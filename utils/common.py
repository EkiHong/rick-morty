import os
import json
import collections.abc
from path import DATA

def deep_update(base_dict: dict, override_dict: dict) -> dict:
    """
    合併兩個字典，將 override_dict 的值覆蓋到 base_dict 中，支援無限層級的巢狀結構。
    """
    for key, value in override_dict.items():
        if isinstance(value, collections.abc.Mapping):
            base_dict[key] = deep_update(base_dict.get(key, {}), value)
        else:
            base_dict[key] = value
    return base_dict

    
def load_test_data(filename: str, api_key: str, env: str = "UAT") -> list:
    """
    通用讀取 JSON 測試資料的輔助函式。
    
    :param filename: JSON 檔名 (不含 .json 後綴，例如 'location', 'json_placeholder')
    :param api_key: JSON 中的頂層 Key (對應 Testcase 名稱)
    :param env: 測試環境，預設為 UAT
    """
    json_file_path = os.path.join(DATA, env, f"{filename}.json")
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            test_data = json.load(f)
        return test_data.get(api_key, [])
    except FileNotFoundError:
        print(f"警告：找不到測試資料檔案 {json_file_path}")
        return []