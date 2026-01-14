import time
from enum import EnumType

import allure
from playwright.sync_api import expect

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
    def test_click_health_metrics_05_002_01(self,page, create_job, open_page):
        folder_job = create_job(self.generator.generate_folder_name(), self.item_type.FOLDER)
        configuration_page = open_page(BaseConfigurationPage,
                                  self.endpoints.JOB_CONFIGURE_URL(folder_job))
        button_hm  = self.locators.BaseConfigurationPageLocators.HEALTH_METRICS
        configuration_page.click(button_hm)
        configuration_page.expect_locator_enabled(button_hm)

    @allure.story("Health metrics")
    def test_tc_05_002_02(page, new_folder):
        pass
        # folder_name = new_folder
        # """Метрики выпадающего списка из acceptance Criteria"""
        # metric = ["Child item with the given name", "Child item with worst health"]
        #
        # health_metric_button_loc = "button[data-section-id='health-metrics']"
        # health_metric_dropdown_button_loc = "button[class*='advancedButton']"
        # add_metric_button_loc = "button[class*='hetero-list-add']"
        # dropdown_text_loc = "button.jenkins-dropdown__item"
        #
        # page.goto(f"/job/{folder_name}/configure")
        # page.click(health_metric_button_loc)
        # page.click(health_metric_dropdown_button_loc)
        # page.click(add_metric_button_loc)
        # """Получить все опции выпадающего меню"""
        # all_options_button = page.locator(dropdown_text_loc).all_inner_texts()
        # """Проверка, что все опции из Acceptance Criteria присутствуют в выпадающем меню"""
        # assert all_options_button == metric