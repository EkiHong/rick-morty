# Rick and Morty API automation framework

## Project info
Base on Python + Pytest for API automation framework.

Using 『Rick and Morty open source API 』to inherit API automation framework

## 架構概述
- 分層架構（Framework -> Unit -> Flow -> Testcase）
- 支援多環境（STG/UAT/PROD）
- 整合 Allure report
- TDD (資料驅動測試)
- 支援同時『單一隻 API 測試 - 快速驗證基本功能 』、『多隻 API 串接測試』

## 環境準備

### install library
```bash
pip install -r requirements.txt
```

### 安裝 Allure 命令列工具（可選）
```bash
# MacOS
brew install allure

# Windows
scoop install allure

# Linux
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

## 專案架構說明

- `framework/`: 底層框架
- `unit/`: API 封裝層
- `flow/`: 業務流程封裝層
- `testcase/`: 測案
- `data/`: 測資
- `env/`: 環境配置
- `utils/`: 工具
- `reports/`: 測報
- `logs/`: log

## 測案說明

### 單一 API 測試
- 取得角色資訊
- 搜尋角色
- 批次取得角色
- 錯誤處理測試

### 業務流程測試
- 角色與地點關聯查詢
- 地點居民查詢流程

### 基本執行
```bash
# run all
python run.py

# assign env
python run.py --env UAT

# exec assign testcase (by file)
python run.py --test testcase/character/test_get_character.py

# exec assign mark testcase
python run.py --marker single
```

### exec by pytest
```bash
# run all testcase
pytest

# exec single testcase
pytest testcase/character/ -v

# exec flow testcase
pytest testcase/flow/ -v

# exec testcase by mark
pytest -m smoke
```

## To Do
- 完善的錯誤處理機制
- log 優化並寫入 allure report
- 逐步優化 pytest.ini
- 加入資料庫驗證、效能測試
- 底層核心 lib 新增 playwright


## 備註
### 新增 API 封裝
1. 在 `unit/` 下建立對應的服務資料夾
2. 繼承 `RickMortyAPI` 類別
3. 實作 API 方法

### 新增測試案例
1. 在 `testcase/` 下建立測試檔案
2. 使用 pytest fixture 管理測試資料
3. 使用 allure 標記增強報告

### 新增業務流程
1. 在 `flow/` 下建立流程類別
2. 組合多個 API 呼叫
3. 實現業務邏輯

### 測試資料引用
1. 測試資料由 conftest.py 讀取
2. Testcase 層呼叫 API 並將測資塞入
3. User 在 Testcase 層使用時，明確知道是呼叫哪隻 API、Flow，明確知道塞入什麼 Testdata 

## 架構設計理念

本框架的核心設計思想是**徹底分離「不變的」與「易變的」**，將底層的技術細節與上層的業務邏輯清晰地解耦。這使得框架易於維護、擴充和閱讀。

### 分層職責劃分

#### 1. 核心底層 (`ABC Class`)


#### 2. 核心框架層 (`RequestAPI`、`PlaywrightAPI`)
- **定位**: 技術基石，處理 **"如何發送請求"** 的技術細節。
- **持有**:
    - `base_url` (例如: `https://rickandmortyapi.com/api`)
    - 通用的 `headers`
    - `requests.Session` 物件，用於保持連線與設定。
- **提供**: `get()`, `post()`, `put()`, `delete()` 等原子性的 HTTP 方法。它不關心業務邏輯，只負責忠實地完成 HTTP 通訊。

#### 2. API 封裝層 (`Unit`)
- **定位**: 業務資源的封裝，處理 **"要請求哪個業務資源"**。
- **持有**:
    - API 的 `path` (例如: `/character`, `/location/{id}`)
    - `payload` 的結構定義。
- **提供**: 具有業務意義的方法，例如 `get_single_character(id)`, `filter_characters(status='alive')`。這些方法內部會去呼叫 `Framework` 層提供的 `get` 或 `post` 方法。

#### 3. 測試案例層 (`Testcase`)
- **定位**: 業務驗證，專注於 **"測什麼"** 和 **"如何驗證"**。
- **職責**:
    - 準備測試資料。
    - 呼叫 `Unit` 層或 `Flow` 層的業務方法。
    - 使用斷言 (assertion) 驗證回傳結果是否符合預期。
- **優勢**: 測試案例的程式碼讀起來就像在讀業務需求，非常直觀，無需關心底層實現。

### 執行流程範例

1.  **初始化 (Setup Phase)**: 在 `conftest.py` 的 `fixture` 中，建立 `Unit` 層的 API 物件 (例如 `CharacterAPI`)。在建立物件時，將固定的 `base_url` 和 `headers` 作為參數傳入，完成底層客戶端的初始化。
2.  **測試執行 (Test Phase)**: 測試案例從 `fixture` 獲取初始化好的 API 物件，直接呼叫其業務方法 (如 `get_single_character(1)`)。
3.  **請求發送**: `Unit` 層的方法會準備好 `path`，並呼叫 `Framework` 層的 `get()` 或 `post()`。`Framework` 層負責將 `base_url` 和 `path` 組合，並使用設定好的 `headers` 發送最終的 HTTP 請求。

透過這樣的設計，當 API 的 `path` 或 `payload` 變更時，我們只需要修改對應的 `Unit` 層類別；如果整個服務的網域變更，只需修改環境配置，從而實現了高度的可維護性。
