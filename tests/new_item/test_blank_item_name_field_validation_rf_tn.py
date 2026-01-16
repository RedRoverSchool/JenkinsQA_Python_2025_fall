from playwright.sync_api import expect
from locators.base_locators import BaseLocators
from locators.new_item_locators import NewItemLocators
from data.endpoints import Endpoints
from conftest import open_page
from pages.base_page import BasePage
from data.data import NewItemPageData
from data.data import ItemTypesData
import pytest



class TestBlankFieldValidation:
    locators = BaseLocators(), NewItemLocators()
    endpoints = Endpoints()


    @pytest.mark.parametrize("item_type", ItemTypesData.ITEM_TYPES)
    def test_tc_01_001_04_blank_item_name_validation_1(self, open_page, page, item_type):
        """TC_01.001.04 | New Item > Create a new item > Validation error when "Enter an item name" field is blank"""

        open_page(BasePage, self.endpoints.ALL_NEW_JOB_URL)
        page.get_by_text(item_type, exact=True).click()
        expect(page.get_by_text(NewItemPageData.EMPTY_ITEM_NAME_VALIDATION_TEXT, exact=True)).to_be_visible()
        expect(page.locator(BaseLocators.OK_BUTTON)).to_be_disabled()
