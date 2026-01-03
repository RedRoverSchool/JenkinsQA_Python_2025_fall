import pytest
from playwright.sync_api import expect
import re


@pytest.fixture
def create_user1(page):
    page.goto("/")

    page.click("a[href='/manage']")

    page.click("a[href='securityRealm/']")

    page.click("a[href='addUser']")

    page.fill("input[name='username']", "User1")
    page.fill("input[name='password1']", "Tim12!")
    page.fill("input[name='password2']", "Tim12!")
    page.fill("input[name='fullname']", "Tim Sagov")
    page.fill("input[name='email']", "tim1@sagov.com")

    page.click("button[name='Submit']")

    yield "User1"

def test_user_create_cancel(create_user1, page):
    page.goto("/securityRealm/")

    page.locator("tr:has-text('User1') td:last-child").click()
    page.click("button[data-id='cancel']")

    expect(page).to_have_url(re.compile(r"/securityRealm/"))