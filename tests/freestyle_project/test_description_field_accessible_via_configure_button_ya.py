from playwright.sync_api import expect
from data.enums import ItemType
from utils.generators.project_generator import ProjectGenerator
from data.endpoints import Endpoints
from locators.freestyle_project_configuration_locators import FreestyleProjectConfigurationLocators
from locators.base_locators import BaseLocators


def test_tc_02_002_02_description_field_accessible_via_configure_button(create_job, page):
    """TC_02.002_02 | Freestyle Project Configuration > Project Description >
    Verify config page with description accessible via Configure button"""

    freestyle_name = ProjectGenerator.generate_freestyle_name()
    create_job(freestyle_name, ItemType.FREESTYLE)
    page.goto(Endpoints().JOB_STATUS_PAGE_URL(freestyle_name))

    page.locator(FreestyleProjectConfigurationLocators.CONFIGURE_BUTTON).click()

    description_field = page.locator(BaseLocators.BaseConfigurationPageLocators.TEXTAREA_DESCRIPTION)
    expect(description_field).not_to_be_disabled()