from playwright.sync_api import expect
from locators.base_locators import BaseLocators

def test_tc_02_002_01_config_page_with_description_accessible(freestyle):
    """
    TC_02.002_01 | Freestyle Project Configuration > Project Description >
    Verify config page with description accessible after creation
    """
    expect(freestyle.locator(BaseLocators.BaseConfigurationPageLocators.TEXTAREA_DESCRIPTION)).to_be_visible()