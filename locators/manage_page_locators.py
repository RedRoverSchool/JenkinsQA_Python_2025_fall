from locators.base_locators import BaseLocators


class ManagePageLocators(BaseLocators):

    SYSTEM_CONFIGURATION_LOC = lambda self, name: f"//dt[normalize-space()='{name}']"
