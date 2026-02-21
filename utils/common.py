import collections.abc
import json

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

def load_json_data(file_path: str) -> dict:
    """讀取 JSON 測試資料的輔助函式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)