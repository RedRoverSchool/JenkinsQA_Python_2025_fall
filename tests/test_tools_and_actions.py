from playwright.sync_api import expect

def test_tools_and_actions(page):
    page.goto("/manage")

    expect(page.get_by_role("heading", name="Tools and Actions")).to_be_visible()

    expect(page.get_by_role("link", name="Reload Configuration from Disk")).to_be_visible()
    expect(page.get_by_role("link", name="Jenkins CLI")).to_be_visible()
    expect(page.get_by_role("link", name="Script Console")).to_be_visible()
    expect(page.get_by_role("link", name="Prepare for Shutdown"))