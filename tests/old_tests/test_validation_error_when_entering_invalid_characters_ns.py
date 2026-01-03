import time
from playwright.sync_api import expect


def test_validation_error_invalid_characters(page):
    page.goto("/")

    invalid_characters = "Test#Item!"

    """Click the “New Item” button."""
    page.locator("a[href='/view/all/newJob']").click()

    """Enter an invalid item name containing forbidden characters (e.g., Test#Item!)."""
    item_name_field_loc = page.locator("input[id='name']")
    item_name_field_loc.fill(invalid_characters)

    item_name_invalid_message_loc = page.locator("div[id='itemname-invalid']")
    text_item_message = item_name_invalid_message_loc.text_content()
    expect(item_name_invalid_message_loc).to_be_visible()

    button_ok_loc = page.locator("button[id='ok-button']")
    expect(button_ok_loc).to_be_disabled()



