from core.config import Config

class Links:
    BASE_URL = f"http://{Config.HOST}:{Config.PORT}"
    CRUMB_URL = f"{BASE_URL}/crumbIssuer/api/json"
    DELETE_URL = BASE_URL + "/job/{}/doDelete"
