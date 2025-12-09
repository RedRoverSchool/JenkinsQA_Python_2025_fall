from playwright.sync_api import expect

def test_tc_11_001_01(page):
    page.goto("/")

    text_title = page.locator('.empty-state-block h1')
    expect(text_title).to_contain_text('Welcome to Jenkins!')
