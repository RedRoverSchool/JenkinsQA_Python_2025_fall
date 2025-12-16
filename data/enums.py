from enum import Enum

class ItemType(str, Enum):
    FREESTYLE = "freestyle"
    PIPELINE ="pipeline"
    MULTI_CONFIGURATION_PROJECT = "multi_configuration_project"
    FOLDER = "folder"
    MULTIBRANCH_PIPELINE = "multibranch_pipeline"
    ORGANIZATION_FOLDER = "organization_folder"






