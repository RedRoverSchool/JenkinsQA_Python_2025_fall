import random

from playwright.sync_api import expect


def test_create_multi_configuration_project_visible_on_dashboard(page):
    project_name = f"Multi-configuration project_{random.randint(1, 1000)}"
    projects_names_loc = "//tr[@id]//a//span"

    page.goto("/")
    page.get_by_role("link", name="New Item").click()

    page.get_by_role("textbox", name="Enter an item name").fill(project_name)
    page.get_by_text("Multi-configuration project", exact=True).click()
    page.get_by_role("button", name="OK").click()

    page.get_by_role("link", name="Jenkins", exact=True).click()

    expect(page.locator(projects_names_loc).filter(has_text=project_name)).to_be_visible()


