import allure

from data.endpoints import Endpoints
from data.enums import ItemType

from pages.new_item_page import NewItemPage
from utils.generators.project_generator import ProjectGenerator


@allure.epic("NewItemPage")
@allure.feature("Handle errors on NewItemPage")
class TestErrorMessageItemName:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    new_item_page = NewItemPage
    item_name = generator.generate_folder_name()

    @allure.story("Error: existing item name")
    def test_tc_01_001_06_error_existing_item_name(self, create_job, open_page):
        job_name = create_job(self.item_name, ItemType.FOLDER)
        all_job_page = open_page(NewItemPage, self.endpoints.ALL_NEW_JOB_URL)
        error_message = all_job_page.create_project_with_existing_name(job_name)

        assert error_message == f"» A job already exists with the name ‘{job_name}’"