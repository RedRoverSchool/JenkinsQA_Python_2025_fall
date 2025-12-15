from pages.freestyle_project_configuration_page import FreestyleProjectConfigurationPage


class TestFreestyleProjectToggle:

    def test_RF_02_001_002_toggle_enable(self, page):

        freestyle_page = FreestyleProjectConfigurationPage(page)

        project_name = freestyle_page.create_freestyle_project_precondition()
        freestyle_page.open_project_configuration(project_name)
        freestyle_page.assert_toggle_is_enabled()