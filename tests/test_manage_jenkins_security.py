from playwright.sync_api import expect

def test_manage_jenkins_security(page):
    page.goto("/manage")

    expect(page.get_by_role("heading", name="Security")).to_be_visible()

    expect(page.get_by_role("link", name="Security"))
    expect(page.get_by_role("link", name="Credentials"))
    expect(page.get_by_role("link", name="Credentials Providers"))
    expect(page.get_by_role("link", name="Users"))