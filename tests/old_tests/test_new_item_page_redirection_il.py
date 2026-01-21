from playwright.sync_api import expect

def test_new_item_page_redirection(page):
    page.goto('/')

    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//a[@href="/view/all/newJob"]')

    new_item_page = page.locator('//span[contains(text(), "New Item")]')
    expect(new_item_page).to_have_text("New Item")