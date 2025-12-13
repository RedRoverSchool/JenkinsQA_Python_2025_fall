import pytest
from playwright.sync_api import expect


@pytest.fixture
def mc1_project(page):
    page.goto("/view/all/newJob")

    page.fill("#name", "MC1")

    page.locator("label:has-text('Multi-configuration project')").click()

    page.locator("button[type='submit']").click()

    page.locator("button[name='Submit']").click()

    yield

def test_delete_cancel_mc1(page, mc1_project):
    page.goto("/")

    page.locator(
        "button.jenkins-menu-dropdown-chevron[data-href*='/job/MC1/']"
    ).click(force=True)

    page.locator("[href*='doDelete']").click()

    page.locator("button[data-id='cancel']").click()

    expect(page).to_have_url("/")