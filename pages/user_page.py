from pages.base_page import BasePage
from locators.user_locators import UserLocators


class UserPage(BasePage):
    loc = UserLocators()

    def delete_user(self, name):
        self.page.click(self.loc.DELETE_USER(name))
        self.page.click(self.loc.CONFIRM_DELETE_USER)

    def get_user_name(self,loc):
        try:
            return loc.get_text()

        except Exception:
            return "User not exists"