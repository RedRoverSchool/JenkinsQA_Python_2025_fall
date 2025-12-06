from playwright.sync_api import expect
from conftest import USER_NAME
import re

def test_user_menu_items(page):

    page.goto("/")

    page.locator(f"a[href='/user/{USER_NAME}']").hover()

    items = page.locator(".jenkins-dropdown__item")

    expected = [
        USER_NAME,
        "Theme",
        "My Views",
        "Account",
        "Appearance",
        "Preferences",
        "Security",
        "Experiments",
        "Credentials",
        "Sign out",
    ]

    expect(items).to_have_count(len(expected))

    for i, text in enumerate(expected):
        expect(items.nth(i)).to_have_text(re.compile(rf".*{text}.*"))