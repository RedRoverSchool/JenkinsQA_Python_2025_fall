from locators.base_locators import BaseLocators


class FreestyleProjectConfigurationLocators(BaseLocators):

    ITEM_NAME_FIELD = "#name"
    FREESTYLE_PROJECT_TYPE = "//span[text()='Freestyle project']"
    HOME_ICON = "#jenkins-head-icon"
    CONFIGURE_BUTTON = "a[href$='configure']"
    TOGGLE_INPUT = "input#enable-disable-project"
    TOGGLE_LABEL = "label[for='enable-disable-project']"
    DISABLED_MESSAGE_TEXT = "This project is currently disabled"
