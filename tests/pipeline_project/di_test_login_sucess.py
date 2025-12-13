from playwright.sync_api import sync_playwright
def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/login")
        page.locator("#j_username").fill("DariaIa")
        page.locator("input[name='j_password']").fill("Solutions89!")
        page.locator("button[name='Submit']").click()
        page.close()
        browser.close()