import allure
from utils.generators.project_generator import ProjectGenerator
from pages.new_item_page import NewItemPage
from locators.new_item_locators import NewItemLocators


@allure.title("TC_01.002.06 | New Item > Folder > Verify unique item name constraint inside a folder")
def test_unique_item_name_constraint(page, create_job, open_page):
    with allure.step("Setup: Create folder and project via API"):
        folder_name = ProjectGenerator.generate_folder_name()
        create_job(name=folder_name, job_type="folder")
        create_job(name="Test_Project", job_type="freestyle", folder=folder_name)

    with allure.step("Test: Try to create duplicate via UI"):
        new_item_page = open_page(NewItemPage, f"/job/{folder_name}/newJob")
        new_item_page.fill(NewItemLocators.NAME_FIELD, "Test_Project")

    with allure.step("Assert: Verify duplicate error"):
        error = new_item_page.get_text(NewItemLocators.ERROR_MESSAGE)
        assert "already exists" in error, f"Expected 'already exists' in: {error}"


