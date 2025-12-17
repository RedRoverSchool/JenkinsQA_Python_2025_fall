from locators.base_locators import BaseLocators

from pages.base_page import BasePage


class BaseProjectPage(BasePage):

    def description_text(self):
        return self.get_text(BaseLocators.BaseProjectPage.DESCRIPTION_TEXT)