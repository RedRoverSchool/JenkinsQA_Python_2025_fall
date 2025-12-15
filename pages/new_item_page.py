from locators.new_item_locators import NewItemLocators
from pages.base_page import BasePage




class NewItemPage(BasePage):
    def open_new_item_page(self):
        self.click(NewItemLocators.NEW_ITEM_BTN)

    def is_new_item_page_opened(self) -> bool:
        self.wait_for_visible(NewItemLocators.SELECT_ITEM_TYPE_SECTION)
        return True
