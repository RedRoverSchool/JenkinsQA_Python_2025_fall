from playwright.sync_api import expect


def test_tc_01_001_08(page):

    page.goto("/")

    # Locators
    new_item_btn_loc = "a[href='/view/all/newJob']"
    new_item_header = "#add-item-panel > h1"
    new_item_breadcrumbs = "#breadcrumbs > li > span"


    page.locator(new_item_btn_loc).click()

    expect(page.locator(new_item_header)).to_be_visible()
    expect(page.locator(new_item_breadcrumbs)).to_have_text("New Item")
    assert page.url.endswith("/view/all/newJob")









