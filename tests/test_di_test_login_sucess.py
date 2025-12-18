import pytest
from playwright.sync_api import expect

@pytest.fixture
def registered_user():

    user = {
        "username": "DariaIa",
        "password": "Assistants89!"
    }
    return user


def test_login_success(page, base_url, registered_user):

    page.goto(f"{base_url}/login")


    page.locator("#j_username").fill(registered_user["username"])
    page.locator("input[name='j_password']").fill(registered_user["password"])
    page.locator("button[name='Submit']").click()

    page.wait_for_url(base_url + "/")
    expect(page.locator("a:has-text('All')").first).to_be_visible(timeout=5000)
