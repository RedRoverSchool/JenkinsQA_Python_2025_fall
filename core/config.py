import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    USER_NAME = os.getenv("JENKINS_USERNAME")
    USER_PASSWORD = os.getenv("JENKINS_PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    HEADLESS_MODE = os.getenv("HEADLESS_MODE", "false").lower() == "true"