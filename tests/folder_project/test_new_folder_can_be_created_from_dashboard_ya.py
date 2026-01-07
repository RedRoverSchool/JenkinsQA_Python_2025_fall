from pages.base_configuration_page import BaseConfigurationPage

def test_tc_01_002_02_new_folder_can_be_created_from_dashboard(page, new_folder, open_page):
    """TC_01.002.02 | New Item > Folder > Verify new folder can be created from dashboard"""

    config_page = open_page(BaseConfigurationPage, f"/job/{new_folder}/configure")
    assert new_folder in config_page.page.title()
