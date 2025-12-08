from playwright.sync_api import expect
def test_new_item_section_visible(page):
    page.goto("http://localhost:8080/login")
    page.fill("#j_username", "DariaIa")
    page.fill("[name='j_password']", "Solutions89!")
    page.click("[name='Submit']")
    page.click("a[href='/view/all/newJob']")
    expect(page.get_by_text("Freestyle project")).to_be_visible()