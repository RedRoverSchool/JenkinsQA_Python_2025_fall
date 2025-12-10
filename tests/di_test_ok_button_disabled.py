from playwright.sync_api import expect
def test_ok_disabled_when_name_empty(page):
    page.goto("http://localhost:8080/login")
    page.fill("#j_username", "DariaIa")
    page.fill("[name='j_password']", "Solutions89!")
    page.click("[name='Submit']")
    page.goto("http://localhost:8080/view/all/newJob")
    expect(page.get_by_role("button", name="OK")).to_be_disabled()

