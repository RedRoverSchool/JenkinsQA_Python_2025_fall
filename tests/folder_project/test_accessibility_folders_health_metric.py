import allure

from data.endpoints import Endpoints
from data.enums import ItemType
from pages.base_configuration_page import BaseConfigurationPage
from locators.base_locators import BaseLocators
from utils.generators.project_generator import ProjectGenerator


@allure.epic("Folder")
@allure.feature("Essential features in folder")
class TestAccessibilityFoldersHealthMetrics:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    locators = BaseLocators()
    item_type = ItemType

    @allure.story("Health metrics")
    def test_click_health_metrics_05_002_01(self, create_job, open_page):
        folder_job = create_job(self.generator.generate_folder_name(), self.item_type.FOLDER)
        configuration_page = open_page(BaseConfigurationPage,
                                       self.endpoints.JOB_CONFIGURE_URL(folder_job))
        button_hm = self.locators.BaseConfigurationPageLocators.HEALTH_METRICS
        configuration_page.click(button_hm)
        configuration_page.expect_locator_enabled(button_hm)

    @allure.story("Health metrics")
    def test_click_health_metrics_tc_05_002_02(self, create_job, open_page):
        folder_job = create_job(self.generator.generate_folder_name(), self.item_type.FOLDER)
        configuration_page = open_page(BaseConfigurationPage,
                                       self.endpoints.JOB_CONFIGURE_URL(folder_job))
        configuration_page.click(self.locators.BaseConfigurationPageLocators.HEALTH_METRICS)
        configuration_page.click(self.locators.BaseConfigurationPageLocators.HEALTH_METRICS_DROPDOWN_BUTTON_LOC)
        configuration_page.click(self.locators.BaseConfigurationPageLocators.ADD_METRIC_BUTTON_LOC)
        inner_text = configuration_page.get_inner_text(self.locators.BaseConfigurationPageLocators.DROPDOWN_TEXT_LOC)

        assert inner_text == ['Child item with the given name', 'Child item with worst health']