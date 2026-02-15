import os
from datetime import datetime

# 專案根目錄
API = os.path.abspath(os.path.dirname(__file__))

# 資料目錄
DATA = os.path.join(API, "data")

# 報告目錄
REPORTS = os.path.join(API, "reports")
if not os.path.exists(REPORTS):
    os.makedirs(REPORTS)

# Log 目錄
LOG = os.path.join(API, "logs")
if not os.path.exists(LOG):
    os.makedirs(LOG)

# 時間戳記
START_TIME = datetime.now().strftime("%Y%m%d_%H%M%S")

# Log 檔案路徑
LOG_FILE = os.path.join(LOG, f'{START_TIME}.log')

# 報告相關路徑
START_TIME_DIR = os.path.join(REPORTS, START_TIME)
ALLURE_TMP = os.path.join(REPORTS, 'allure_tmp')
ALLURE_INDEX = os.path.join(START_TIME_DIR, 'allure_index')

# 建立必要目錄
for directory in [START_TIME_DIR, ALLURE_TMP]:
    if not os.path.exists(directory):
        os.makedirs(directory)