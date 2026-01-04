from playwright.sync_api import expect


def test_status_information(page):
    page.goto("/manage")

    expect(page.get_by_role("heading", name="Status Information"))

    expect(page.get_by_role("link", name="System Information")).to_be_visible()
    expect(page.get_by_role("link", name="System Log")).to_be_visible()
    expect(page.get_by_role("link", name="Load Statistics")).to_be_visible()
    expect(page.get_by_role("link", name="About Jenkins")).to_be_visible()