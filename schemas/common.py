from typing import TypeVar, Generic
from pydantic import HttpUrl
from schemas.base import APIResponseBase

# 宣告一個泛型代名詞 T (代表 Type)
T = TypeVar('T')

class PageInfo(APIResponseBase):
    count: int
    pages: int
    # 使用 | None 來表示這個欄位可能是 HttpUrl，也可能是 null (Python 中的 None)
    next: HttpUrl | None
    prev: HttpUrl | None

# 建立泛型的外殼，繼承 Generic[T] 是關鍵！
class PaginatedResponse(APIResponseBase, Generic[T]):
    info: PageInfo
    
    # 這裡告訴 Pydantic：results 是一個陣列，裡面裝的東西型別是 T
    # T 是什麼？等別人使用這個模型時會告訴你。
    results: list[T]