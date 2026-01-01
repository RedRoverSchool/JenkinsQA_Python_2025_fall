from playwright.sync_api import expect
def test_login_success(page):
    page.goto("http://localhost:8080/login")
    page.fill("#j_username", "DariaIa")
    page.fill("[name='j_password']", "Solutions89!")
    page.click("[name='Submit']")
    expect(page).to_have_url("http://localhost:8080/")