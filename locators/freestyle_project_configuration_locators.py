from locators.base_locators import BaseLocators


# файл legacy
class FreestyleProjectConfigurationLocators(BaseLocators):

    ITEM_NAME_FIELD = "#name"
    FREESTYLE_PROJECT_TYPE = "//span[text()='Freestyle project']"
    HOME_ICON = "#jenkins-head-icon"
    CONFIGURE_BUTTON = "a[href$='configure']"
