from playwright.sync_api import expect

def test_enter_an_item_name_field(page):
    page.goto('/')

    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//a[@href="/view/all/newJob"]')

    item_name_page = page.locator('//label[contains(text(), "Enter an item name")]')
    expect(item_name_page).to_have_text("Enter an item name")

    input_field = page.locator('//input[@id="name"]')
    expect(input_field).to_be_visible()

