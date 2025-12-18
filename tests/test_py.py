from playwright.sync_api import sync_playwright

def test_playwright_browsers_available():
    with sync_playwright() as p:
        assert p.chromium is not None
        assert p.firefox is not None
        assert p.webkit is not None