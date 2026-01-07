import time

from playwright.sync_api import expect
def test_validation_valid_characters(page):
    """URL"""
    page.goto("/")

    alphanumeric_characters_underscores = "Jen_test123"

    page.locator('//a[@href="/view/all/newJob"]').click()
    time.sleep(3)

    item_name_field_loc = page.locator('//input[@id="name"]')
    item_name_field_loc.fill(alphanumeric_characters_underscores)

    expect(item_name_field_loc).to_be_visible()





