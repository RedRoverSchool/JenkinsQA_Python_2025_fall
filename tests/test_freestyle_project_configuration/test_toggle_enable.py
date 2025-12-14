from pages.freestyle_project_configuration_page import FreestyleProjectConfigurationPage


class TestFreestyleProjectToggle:

    def test_RF_02_001_002_toggle_enable(self, page):
        project_name = "Freestyle_222914"

        freestyle_page = FreestyleProjectConfigurationPage(page, f"/job/{project_name}/configure")
        freestyle_page.open()
        freestyle_page.assert_toggle_is_enabled()
