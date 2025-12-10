import re
from playwright.sync_api import expect

def test_user_gets_access(page):
    page.goto("/manage/securityRealm/")

    user_dropdown = page.locator("#root-action-UserAction")
    user_dropdown.hover()

    page.get_by_role("link", name="Account").click()

    page.wait_for_timeout(5000)

    expect(page).to_have_url(re.compile(r"/user/tim/account/?"))