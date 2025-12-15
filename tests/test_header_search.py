import re
from playwright.sync_api import expect


def test_verify_header_search_functionality(page):

    page.goto("/")

    search_box = page.locator("#search-box")

    query = "test_query"

    search_box.fill(query)
    search_box.press("Enter")

    expect(page).to_have_url(re.compile("/search/"))

    header = page.locator("h1")
    expect(header).to_contain_text(f"Search for '{query}'")