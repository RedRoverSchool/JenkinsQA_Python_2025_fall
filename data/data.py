

class BaseConfigurationPageData:
    DISABLED_MESSAGE_TEXT = "This project is currently disabled"

class ManageJenkinsData:
    STATUS_INFORMATION = ["System Information", "System Log", "Load Statistics", "About Jenkins"]

    TOOLS_AND_ACTIONS = ["Reload Configuration from Disk", "Jenkins CLI", "Script Console", "Prepare for Shutdown"]

class ItemTypesData:
    ITEM_TYPES = [
        "Freestyle project",
        "Pipeline",
        "Multi-configuration project",
        "Folder",
        "Multibranch Pipeline",
        "Organization Folder",
    ]

class NewItemPageData:
    EMPTY_ITEM_NAME_VALIDATION_TEXT = "» This field cannot be empty, please enter a valid name"
