def get_env_config():
    """
    回傳環境配置。
    在真實的場景中，這裡可能會從 .env 檔案、系統環境變數或遠端配置中心讀取。
    """
    return {
        "base_url": "https://rickandmortyapi.com/api",
        "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    }
