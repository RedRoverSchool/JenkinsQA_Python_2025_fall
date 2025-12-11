from playwright.sync_api import expect

def test_delete_cancel_mc1(page):
    page.goto("/")

    page.locator("button[aria-expanded='false']").first.click(force=True)

    page.locator("text=Delete Multi-configuration Project").click()

    page.locator("button[data-id='cancel']").click()

    expect(page).to_have_url("/")