import allure

from data.endpoints import Endpoints
from pages.new_item_page import NewItemPage
from locators.new_item_locators import NewItemLocators
from utils.generators.project_generator import ProjectGenerator


@allure.epic("New Item")
@allure.feature("Item type selection")
class TestPipelineTypeVisualSelection:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    new_item_page = NewItemPage

    @allure.story("Visual selection of Pipeline type")
    @allure.title("TC_01.004.02 Verify visual selection of Pipeline type")
    def test_tc_01_004_02_pipeline_type_visual_selection(self, page, open_page):
        pipeline_name = self.generator.generate_pipeline_name()
        new_item_page = open_page(self.new_item_page, self.endpoints.ALL_NEW_JOB_URL)
        new_item_page.fill(NewItemLocators.NAME_FIELD, pipeline_name)
        new_item_page.click(NewItemLocators.PIPELINE_TYPE)

        pipeline_element = new_item_page.page.locator(NewItemLocators.PIPELINE_TYPE)
        assert "active" in pipeline_element.get_attribute("class")