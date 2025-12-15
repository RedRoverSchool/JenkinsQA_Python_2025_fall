from playwright.sync_api import expect


def test_verify_page_is_loaded(page):

    page.goto("/")

    logo = page.locator("#jenkins-home-link")
    expect(logo).to_be_visible()