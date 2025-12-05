import time
from playwright.sync_api import expect

def test_validation_error_invalid_characters(page):
    page.goto("/")

    invalid_item_name = "TimItem12!"

    page.locator("a[href='/view/all/newJob']").click()

    item_name_field_loc = page.locator("input[id='name']")
    item_name_field_loc.fill(invalid_item_name)

    item_name_invalid_message_loc = page.locator("[id='itemname-invalid']")
    item_name_invalid_message_loc.text_content()

    expect(item_name_invalid_message_loc).to_contain_text("» ‘!’ is an unsafe character")
    expect(item_name_invalid_message_loc).to_be_visible()

    button_ok_loc = page.locator("[id='ok-button']")
    expect(button_ok_loc).to_be_disabled()
