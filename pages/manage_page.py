from locators.manage_page_locators import ManagePageLocators
from pages.base_page import BasePage


class ManageJenkinsPage(BasePage):
    locators = ManagePageLocators()

    def asd(self, name):
        text = self.get_text(self.locators.SYSTEM_CONFIGURATION_LOC(name))
        return text

    def get_tools_and_actions_item_text(self, name:str)-> str:
        return self.get_text(self.locators.SYSTEM_CONFIGURATION_LOC(name))