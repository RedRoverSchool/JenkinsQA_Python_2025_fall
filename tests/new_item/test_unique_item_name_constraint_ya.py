import allure

from data.endpoints import Endpoints
from data.enums import ItemType
from pages.new_item_page import NewItemPage
from locators.new_item_locators import NewItemLocators
from utils.assertions import Assertions
from utils.generators.project_generator import ProjectGenerator


@allure.epic("New Item")
@allure.feature("Item name validation")
class TestUniqueItemName:
    endpoints = Endpoints()
    assertions = Assertions()
    generator = ProjectGenerator()

    @allure.story("Unique item name constraint inside a folder")
    @allure.title("TC_01.002.06 Verify unique item name constraint inside a folder")
    def test_unique_item_name_constraint(self, page, create_job, open_page):
        folder_name = self.generator.generate_folder_name()
        freestyle_name = self.generator.generate_freestyle_name()

        create_job(name=folder_name, job_type=ItemType.FOLDER)
        create_job(name=freestyle_name, job_type=ItemType.FREESTYLE, folder=folder_name)

        duplicate_page = open_page(NewItemPage, f"{self.endpoints.JOB_STATUS_PAGE_URL(folder_name)}/newJob")
        duplicate_page.fill(NewItemLocators.NAME_FIELD, freestyle_name)

        duplicate_page.wait_for_visible(NewItemLocators.ERROR_MESSAGE, timeout=5000)

        error = duplicate_page.get_text(NewItemLocators.ERROR_MESSAGE)
        self.assertions.assert_text("already exists", error)