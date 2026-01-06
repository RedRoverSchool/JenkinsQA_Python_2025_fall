from pathlib import Path

import requests

from data.enums import ItemType


BASE_DIR = Path(__file__).resolve().parent.parent

def load_xml(item_type_data):
    XML_DIR = BASE_DIR / "data" / "xml"
    item_type = {
        ItemType.FREESTYLE: XML_DIR / "freestyle.xml",
        ItemType.PIPELINE: XML_DIR / "pipeline.xml",
        ItemType.MULTI_CONFIGURATION_PROJECT: XML_DIR / "multi_configuration_project.xml",
        ItemType.FOLDER: XML_DIR / "folder.xml",
        ItemType.MULTIBRANCH_PIPELINE: XML_DIR / "multibranch_pipeline.xml",
        ItemType.ORGANIZATION_FOLDER: XML_DIR / "organization_folder.xml"
    }
    return item_type[item_type_data].read_text(encoding="utf-8")

def execute_user_groovy_script(url: str, groovy_scripts: str, username: str, jenkins_token: str):
    requests.post(
        url=f"{url}/scriptText",
        auth=(username, jenkins_token),
        data={"script": groovy_scripts}
    )


