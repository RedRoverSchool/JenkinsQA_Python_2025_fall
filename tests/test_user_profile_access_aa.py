from playwright.sync_api import expect
from conftest import USER_NAME
import re

def test_user_menu_items(page):

    page.goto("/")

    page.locator(f"a[href='/user/{USER_NAME}']").hover()

    items = page.locator(".jenkins-dropdown__item")

    texts_raw = items.all_inner_texts() or []
    texts = [t.lower() for t in texts_raw]

    expected_common = [
        str(USER_NAME).lower(),
        "my views",
        "account",
        "appearance",
        "preferences",
        "security",
        "experiments",
        "credentials",
        "sign out",
    ]

    for text in expected_common:
        assert any(text in t for t in texts)