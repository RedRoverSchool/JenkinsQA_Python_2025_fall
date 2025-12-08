from playwright.sync_api import sync_playwright, expect

def test_ok_disabled_when_name_empty():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=False).new_page()

        page.goto("http://localhost:8080/login")
        page.fill("#j_username", "DariaIa")
        page.fill("input[name='j_password']", "Solutions89!")
        page.click("button[name='Submit']")
        page.wait_for_url("http://localhost:8080/")


        page.click("text=New Item")
        page.wait_for_url("**/view/all/newJob")

        page.fill("#name", "")
        page.click("text=Pipeline")

        expect(page.locator("#ok-button")).to_be_disabled()
        page.close()


