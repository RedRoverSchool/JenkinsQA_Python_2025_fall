import pytest
from playwright.sync_api import Playwright, ViewportSize
from core import JenkinUtils, Config, Links

@pytest.fixture(scope="session")
def get_cookie(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(
        base_url=Links.BASE_URL
    )
    page = context.new_page()

    name_loc = "input[id='j_username']"
    password_loc = "input[id='j_password']"
    submit_btn_loc = "button[name='Submit']"
    page.goto("/")
    page.locator(name_loc).fill(Config.USER_NAME)
    page.locator(password_loc).fill(Config.USER_PASSWORD)
    page.locator(submit_btn_loc).click()
    cookies = context.cookies()
    page.close()
    context.close()
    browser.close()

    return cookies

@pytest.fixture()
def page(playwright: Playwright, get_cookie):
    browser = playwright.chromium.launch(headless=Config.HEADLESS_MODE)
    context = browser.new_context(
        viewport=ViewportSize(width=1920, height=1200),
        base_url=Links.BASE_URL
    )
    context.add_cookies(get_cookie)
    page = context.new_page()
    jenkins_utils = JenkinUtils()
    yield page
    page.close()
    context.close()
    browser.close()

    jenkins_utils.delete_all_jobs()
