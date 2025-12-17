from playwright.sync_api import expect


def test_login_success(page, base_url):

    page.goto(f"{base_url}/login")
    page.locator("#j_username").fill("DariaIa")
    page.locator("input[name='j_password']").fill("Assistants89!")
    page.locator("button[name='Submit']").click()


    page.wait_for_url(base_url + "/")


    expect(page.locator("a:has-text('All')").first).to_be_visible(timeout=5000)