import os
import pytest
import requests
from playwright.sync_api import Playwright, ViewportSize, Page
from dotenv import load_dotenv

from data.user.user import create_user_script, delete_user_script
from pages.base_configuration_page import BaseConfigurationPage
from pages.base_project_page import BaseProjectPage
from utils.functions import load_xml, execute_user_groovy_script
from utils.generators.user_generator import UserGenerator
from utils.jenkins_client import JenkinsAPI

load_dotenv()
user_generator = UserGenerator()
USER_NAME = os.getenv("JENKINS_USERNAME")
USER_PASSWORD = os.getenv("JENKINS_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
HEADLESS_MODE = os.getenv("HEADLESS_MODE", "false").lower() == "true"
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")

BASE_URL = f"http://{HOST}:{PORT}"

@pytest.fixture(scope="session")
def jenkins():
    return JenkinsAPI(
        base_url=BASE_URL,
        user=USER_NAME,
        token=JENKINS_TOKEN
    )

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
        viewport=ViewportSize(width=1440, height=960),
        base_url=BASE_URL,
        locale="en-US",
        timezone_id="UTC"
    )
    context.add_cookies(get_cookie)
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture
def create_job(jenkins):
    def _create(name, job_type=None, folder=None):
        xml = load_xml(job_type)
        jenkins.create_item_from_file(
            name=name,
            config_xml=xml,
            folder=folder
        )
        return name
    return _create

def get_all_jobs():
    response = requests.get(
        url=f"{BASE_URL}/api/json",
        auth=(USER_NAME, JENKINS_TOKEN)
    )
    return response.json()['jobs']

def delete_jobs():
    jobs_list = get_all_jobs()

    for job in jobs_list:
        name = job["name"]
        requests.post(
            url=f"{BASE_URL}/job/{name}/doDelete",
            auth=(USER_NAME, JENKINS_TOKEN)
        )

def delete_user(username):
    groovy_script = delete_user_script(username)
    execute_user_groovy_script(
        url=BASE_URL,
        groovy_scripts=groovy_script,
        username=USER_NAME,
        jenkins_token=JENKINS_TOKEN
    )


@pytest.fixture(scope="function", autouse=True)
def delete_jobs_after_all_tests():
    yield
    delete_jobs()

# @pytest.fixture()
# def base_configuration_page(page:Page):
#     return BaseConfigurationPage(page)
#
# @pytest.fixture()
# def base_project_page(page:Page):
#     return BaseProjectPage(page)

@pytest.fixture
def create_user_fixture():
    user_info = next(user_generator.create_user_generator())
    groovy_script = create_user_script(
        username=user_info.username,
        password=user_info.password,
        full_name=user_info.fullname,
        email=user_info.email
    )
    execute_user_groovy_script(
        url=BASE_URL,
        groovy_scripts=groovy_script,
        username=USER_NAME,
        jenkins_token=JENKINS_TOKEN
    )
    yield user_info
    delete_user(user_info.username)


@pytest.fixture
def open_page(page):
    def _open(page_class, url):
        class_page = page_class(page, url)
        class_page.open()
        return class_page
    return _open