from playwright.sync_api import expect


def test_select_item_type(page):
    page.goto("/")

    page.locator("a[href='/view/all/newJob']").click()
    expect(page.locator("div.jenkins-form-label")).to_be_visible()