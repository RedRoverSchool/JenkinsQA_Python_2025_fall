from pages.freestyle_project_configuration_page import (FreestyleProjectConfigurationPage)


class TestFreestyleProjectToggleDisable:

    def test_RF_02_001_003_toggle_disable_error_message(self, page):
        """
        RF_02.001.003 |Freestyle Project Configuration >Toggle Disable – Error message displayed
        """
        freestyle_page = FreestyleProjectConfigurationPage(page)

        project_name = freestyle_page.create_freestyle_project_precondition()
        freestyle_page.open_project_configuration(project_name)
        freestyle_page.disable_project()
        freestyle_page.save_configuration()

        freestyle_page.assert_project_disabled_message_is_displayed()
