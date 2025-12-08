from playwright.sync_api import sync_playwright, expect
import re
def test_ok_disabled_when_name_empty():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/login")
        page.locator("#j_username").fill("DariaIa")
        page.locator("input[name='j_password']").fill("Solutions89!")
        page.locator("button[name='Submit']").click()
        page.wait_for_url("http://localhost:8080/")
        page.locator("span.task-link-text:has-text('New Item')").click()
        page.wait_for_url(re.compile(r".*/view/all/newJob"))
        page.locator("#name").fill("")
        page.get_by_text("Pipeline", exact=True).first.click()
        expect(page.locator("#ok-button")).to_be_disabled(timeout=10000)
        page.close()
        browser.close()

