import random

import pytest
from playwright.sync_api import expect

@pytest.fixture
def create_multi_conf_project(page):
    project_name = f"Multi-configuration project_{random.randint(1, 1000)}"

    page.goto("/")
    page.get_by_role("link", name="New Item").click()
    page.get_by_role("textbox", name="Enter an item name").fill(project_name)
    page.get_by_text("Multi-configuration project", exact=True).click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("link", name="Jenkins", exact=True).click()

    return project_name



