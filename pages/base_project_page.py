from pages.base_page import BasePage


class BaseProjectPage(BasePage):

    def description_text(self, description_text):
        return self.get_text(f"//*[text()= '{description_text}']")