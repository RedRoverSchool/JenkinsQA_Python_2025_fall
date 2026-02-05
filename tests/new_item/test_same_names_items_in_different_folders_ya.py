import allure

from data.endpoints import Endpoints
from data.enums import ItemType
from pages.new_item_page import NewItemPage
from locators.new_item_locators import NewItemLocators
from utils.generators.project_generator import ProjectGenerator


@allure.epic("New Item")
@allure.feature("Item Creation in Folders")
class TestSameNameItemsInDifferentFolders:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    item_type = ItemType
    locators = NewItemLocators()

    def _create_project_in_folder(self, open_page, folder_name, project_name):
        new_item_page = open_page(NewItemPage, self.endpoints.FOLDER_NEW_ITEM_URL(folder_name))
        new_item_page.page.locator(self.locators.NAME_FIELD).fill(project_name)
        new_item_page.page.locator(self.locators.FREESTYLE_PROJECT_TYPE).click()
        new_item_page.page.locator(self.locators.OK_BUTTON).click()

        new_item_page.page.wait_for_url(f"**/job/{project_name}/**")
        return new_item_page

    @allure.story("Same name items in different folders")
    @allure.title("TC_01.002.07 Verify items with identical names can exist in different folders")
    def test_tc_01_002_07_same_names_items_in_different_folders(self, page, create_job, open_page):
        folder_1 = self.generator.generate_folder_name()
        folder_2 = self.generator.generate_folder_name()
        project_name = self.generator.generate_freestyle_name()

        create_job(folder_1, self.item_type.FOLDER)
        create_job(folder_2, self.item_type.FOLDER)

        self._create_project_in_folder(open_page, folder_1, project_name)
        config_page_2 = self._create_project_in_folder(open_page, folder_2, project_name)

        assert f"/job/{folder_2}/job/{project_name}/" in config_page_2.page.url