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

def test_user_profile_page(page):

    page.goto("/")

    page.locator(f"a[href='/user/{USER_NAME}']").click()

    user_icon = page.locator("svg.jenkins-avatar").first
    user_name = page.get_by_role("heading", name=re.compile(rf".*{USER_NAME}.*", re.IGNORECASE)).first
    description_link = page.locator("a#description-link")
    description_textarea = page.locator("textarea[name='description']")

    expect(user_icon).to_be_visible()
    expect(user_name).to_have_text(re.compile(rf".*{USER_NAME}.*"))

    description_link.click(force=True)
    expect(description_textarea).to_be_visible()

    user_id_label = page.locator("text=Jenkins User ID")
    expect(user_id_label).to_be_visible()
    expect(user_id_label).to_have_text(re.compile(rf".*{USER_NAME}.*"))

    items = page.locator("#tasks a")

    sidebar_texts_raw = items.all_inner_texts() or []
    sidebar_texts = [t.lower() for t in sidebar_texts_raw]

    expected_sidebar = [
        "status",
        "builds",
        "my views",
        "account",
        "appearance",
        "preferences",
        "security",
        "experiments",
        "credentials",
    ]

    for name in expected_sidebar:
        assert any(name in t for t in sidebar_texts)