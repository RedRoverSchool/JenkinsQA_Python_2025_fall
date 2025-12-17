import time

from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from pages.create_new_page import CreateNewItemPage
from tests.pipeline_project.conftest import create_new_item


class TestCreateProjectWithoutDescription:

    def test_create_project(self,page):
        create_page = CreateNewItemPage(page)
        create_page.open("/")
        time.sleep(5000)
        # create_page.create_new_project("Test", "pipeline")





    # new_job_link_loc = "//a[@href='newJob']"
    # item_name_field_loc = "//input[@id='name']"
    # pipeline_link_loc = "//div/label/span[text()='Pipeline']"
    # ok_button_loc = "//button[@id='ok-button']"

    # self
    # page.goto("/")
    # page.locator(new_job_link_loc).click()
    # page.locator(item_name_field_loc).fill(project_name)
    # page.locator(pipeline_link_loc).click()
    # page.locator(ok_button_loc).click()
    #
    # page.get_by_role("link", name="Jenkins", exact=True).click()
    #
    # expect(page.get_by_role("link", name=project_name, exact=True)).to_be_visible()