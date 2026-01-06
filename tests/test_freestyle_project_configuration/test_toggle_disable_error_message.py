from data.enums import ItemType


class TestProjectToggleDisable:

    def test_RF_02_001_003_toggle_disable_error_message(self, create_job, base_configuration_page):
        project_name = create_job(
            name="test_job",
            job_type=ItemType.FREESTYLE
        )

        base_configuration_page.go_to_configuration_page(project_name)
        base_configuration_page.disable_project()
        base_configuration_page.save_configuration()

