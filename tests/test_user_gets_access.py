from playwright.sync_api import expect


def test_user_gets_access(page):
    page.goto("http://localhost:8080/manage/securityRealm/")

    user_dropdown = page.locator("a[data-dropdown='true'][href='/user/tim']")
    user_dropdown.hover()

    page.get_by_role("link", name="Account").click()

    page.wait_for_timeout(5000)

    expect(page.url).to_contain("/user/tim/account/")