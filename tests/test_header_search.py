import re
import pytest
from playwright.sync_api import expect
@pytest.mark.skip(reason="Auth fails on CI environment")

def test_verify_header_search_functionality(page):

    page.goto("/")


    search_box = page.locator("input[name='q']")

    query = "test_query"


    search_box.fill(query)
    search_box.press("Enter")


    expect(page).to_have_url(re.compile("/search/"))


    header = page.locator("#main-panel h1")
    expect(header).to_contain_text(f"Search for '{query}'")