import random
from playwright.sync_api import Page, expect


REQUIRED_LINKS = [
    "Status",
    "Configure",
    "+New Item",
    "Delete Folder",
    "Build History",
    "Rename",
    "Credentials"
]

def test_folder_side_panel_navigation(page: Page):
    page.goto("/")

    new_folder_name = f"Test_folder_{random.randint(0, 999999)}"
    page.get_by_role("link", name="New Item").click()
    page.locator("input#name").fill(new_folder_name)
    page.get_by_text("Folder", exact=True).click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("button", name="Save").click()

    expect(page.locator("h1.job-index-headline")).to_have_text(new_folder_name)

    page.goto(f"/job/{new_folder_name}/configure")
    page.wait_for_load_state("domcontentloaded")
    page.goto(f"/job/{new_folder_name}/")

    expect(page.get_by_role("heading", name=new_folder_name, exact=True)).to_be_visible()

    status_link = page.locator("#side-panel").get_by_role("link", name="Status", exact=True)

    expect(status_link).to_be_visible()
    expect(status_link).to_be_enabled()

    side_panel = page.locator("#side-panel")
    for link_text in REQUIRED_LINKS:
        if link_text == "+New Item":
            # New Item link uses href pattern
            link_locator = side_panel.locator("a[href*='newJob']")
        else:
            link_locator = side_panel.get_by_role("link", name=link_text, exact=True)

        expect(link_locator).to_be_visible()
        expect(link_locator).to_be_enabled()
