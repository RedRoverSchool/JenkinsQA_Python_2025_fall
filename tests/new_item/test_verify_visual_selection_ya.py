from pages.new_item_page import NewItemPage
from locators.new_item_locators import NewItemLocators
from utils.generators.project_generator import ProjectGenerator


def test_tc_01_004_02_pipeline_type_visual_selection(page, open_page):
    """TC_01.004.02 | New Item > Select an Item type > Verify visual selection of Pipeline type"""

    new_item_page = open_page(NewItemPage, "/view/all/newJob")
    new_item_page.fill(NewItemLocators.NAME_FIELD, ProjectGenerator.generate_pipeline_name())
    new_item_page.click(NewItemLocators.PIPELINE_TYPE)

    pipeline_element = new_item_page.page.locator(NewItemLocators.PIPELINE_TYPE)
    assert "active" in pipeline_element.get_attribute("class")


