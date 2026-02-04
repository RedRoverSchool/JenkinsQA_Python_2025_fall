import allure

from data.endpoints import Endpoints
from data.enums import ItemType
from pages.base_page import BasePage
from utils.generators.project_generator import ProjectGenerator
from locators.dashboard_locators import DashboardLocators


@allure.epic("New Item")
@allure.feature("Folder visualization")
class TestFolderIconOnDashboard:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    base_page = BasePage

    @allure.story("Folder has distinct icon")
    @allure.title("TC_01.002.05 Verify folder has a distinct icon on the dashboard")
    def test_tc_01_002_05_folder_has_distinct_icon(self, page, create_job, open_page):
        folder_name = self.generator.generate_folder_name()
        create_job(folder_name, ItemType.FOLDER)
        dashboard_page = open_page(self.base_page, self.endpoints.VIEW_ALL_PAGE_URL)

        locator = DashboardLocators.folder_with_icon(folder_name)
        assert dashboard_page.page.locator(locator).is_visible()