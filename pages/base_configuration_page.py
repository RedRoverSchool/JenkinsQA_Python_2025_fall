from pages.base_page import BasePage
from locators.base_locators import BaseLocators


class BaseConfigurationPage(BasePage):

    def go_to_configuration_page(self, name):
        self.page.goto(f"/job/{name}/configure")

    def set_or_change_description(self, text):
        self.fill(BaseLocators.BaseConfigurationPageLocators.TEXTAREA_DESCRIPTION, text)

    def apply_changes(self):
        self.click(BaseLocators.BaseConfigurationPageLocators.BUTTON_APPLY)