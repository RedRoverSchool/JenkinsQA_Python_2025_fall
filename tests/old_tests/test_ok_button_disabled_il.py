from playwright.sync_api import expect

def test_enter_an_item_name_field(page):
    page.goto('/')

    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//a[@href="/view/all/newJob"]')

    item_name_input = page.locator('//input[@id="name"]')
    expect(item_name_input).to_have_text("")

    ok_button = page.locator('//button[@id="ok-button"]')
    expect(ok_button).to_be_disabled()

