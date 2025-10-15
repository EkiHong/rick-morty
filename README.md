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

