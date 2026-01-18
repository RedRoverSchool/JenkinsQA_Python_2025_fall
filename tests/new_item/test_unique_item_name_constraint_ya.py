import allure
from locators.new_item_locators import NewItemLocators
from .unique_item_name_class_test import TestUniqueItemName


@allure.title("TC_01.002.06 | New Item > Folder > Verify unique item name constraint inside a folder")
def test_unique_item_name_constraint(page, create_job, open_page):
    name_validator = TestUniqueItemName()

    folder, freestyle = name_validator.setup_unique_item_name(create_job)
    duplicate_page = name_validator.attempt_duplicate_creation(open_page, folder, freestyle)

    page.wait_for_timeout(3000)

    error = duplicate_page.get_text(NewItemLocators.ERROR_MESSAGE)
    assert "already exists" in error, f"Expected 'already exists' in: {error}"