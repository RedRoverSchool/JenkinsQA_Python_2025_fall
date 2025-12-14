class TestFreestyleProjectToggle:
    def test_RF_02_001_002_toggle_enable(self, freestyle_project_configuration_page):

        project_name = freestyle_project_configuration_page.create_freestyle_project_precondition()

        freestyle_project_configuration_page.open_project_configuration(project_name)

        freestyle_project_configuration_page.assert_toggle_is_visible()
        freestyle_project_configuration_page.assert_toggle_is_enabled()
