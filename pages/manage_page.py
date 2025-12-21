from locators.manage_page_locators import ManagePageLocators
from pages.base_page import BasePage


class ManageJenkinsPage(BasePage):
    locators = ManagePageLocators()

    def asd(self, name):
        text = self.get_text(self.locators.SYSTEM_CONFIGURATION_LOC(name))
        return text