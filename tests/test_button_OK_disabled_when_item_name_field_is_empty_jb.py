from playwright.sync_api import expect

def test_tc_01_001_05_create_new_item(page):
    page.goto("/")

    # Click the "New Item" button
    new_item_link = page.locator("a[href='/view/all/newJob']")
    new_item_link.click()

    # Leave the "Enter an item name" field empty
    item_name_field = page.locator("input[id='name']")
    expect(item_name_field).to_be_visible()
    item_name_field.fill("")

    ok_btn = page.locator("button[id='ok-button']")
    expect(ok_btn).to_be_disabled()