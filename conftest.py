import os
import pytest
from playwright.sync_api import Playwright, ViewportSize
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("JENKINS_USERNAME")
USER_PASSWORD = os.getenv("JENKINS_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
HEADLESS_MODE = os.getenv("HEADLESS_MODE", "false").lower() == "true"


BASE_URL = f"http://{HOST}:{PORT}"

@pytest.fixture(scope="session")
def get_cookie(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(
        base_url=BASE_URL
    )
    page = context.new_page()

    name_loc = "input[id='j_username']"
    password_loc = "input[id='j_password']"
    submit_btn_loc = "button[name='Submit']"
    page.goto("/")
    page.locator(name_loc).fill(USER_NAME)
    page.locator(password_loc).fill(USER_PASSWORD)
    page.locator(submit_btn_loc).click()
    cookies = context.cookies()
    page.close()
    context.close()
    browser.close()

    return cookies

@pytest.fixture()
def page(playwright: Playwright, get_cookie):
    browser = playwright.chromium.launch(headless=HEADLESS_MODE)
    context = browser.new_context(
        viewport=ViewportSize(width=1920, height=1200),
        base_url=BASE_URL
    )
    context.add_cookies(get_cookie)
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()