from playwright.sync_api import expect


def test_verify_page_is_loaded(page):

    page.goto("/")

    expect(page).to_have_title(re.compile("Jenkins"))