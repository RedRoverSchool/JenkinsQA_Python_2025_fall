import allure

from data.endpoints import Endpoints
from data.enums import ItemType
from pages.base_configuration_page import BaseConfigurationPage
from utils.generators.project_generator import ProjectGenerator


@allure.epic("New Item")
@allure.feature("Folder creation")
class TestFolderCreationFromDashboard:
    endpoints = Endpoints()
    generator = ProjectGenerator()

    @allure.title("TC_01.002.02 Verify new folder can be created from dashboard")
    def test_tc_01_002_02_new_folder_can_be_created_from_dashboard(self, page, create_job, open_page):
        folder_name = self.generator.generate_folder_name()
        create_job(folder_name, job_type=ItemType.FOLDER)

        config_url = self.endpoints.JOB_CONFIGURE_URL(folder_name)
        config_page = open_page(BaseConfigurationPage, config_url)

        assert folder_name in config_page.page.title()