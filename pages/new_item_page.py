import allure

from locators.base_locators import BaseLocators
from locators.new_item_locators import NewItemLocators
from pages.base_page import BasePage

loc = NewItemLocators()
class NewItemPage(BasePage):

    def open_new_item_page(self):
        self.open()
        self.click(NewItemLocators.NEW_ITEM_BTN)

    def is_new_item_page_opened(self) -> bool:
        self.wait_for_visible(NewItemLocators.SELECT_ITEM_TYPE_SECTION)
        return self.is_visible(NewItemLocators.SELECT_ITEM_TYPE_SECTION)

    def create_project_with_existing_name(self, name):
        with allure.step(f"Enter existing item name: {name}"):
            self.page.fill(loc.NAME_FIELD, name)
            return self.page.locator(NewItemLocators.ERROR_MESSAGE).inner_text()





