from data.endpoints import Endpoints
from data.enums import ItemType
from pages.base_configuration_page import BaseConfigurationPage
from utils.generators.project_generator import ProjectGenerator


class TestItem:

    generator = ProjectGenerator()
    item_type = ItemType
    endpoints = Endpoints()

    def test_rf_02_001_003_toggle_disable_error_message(self, create_job, open_page):
        job_name = create_job(self.generator.generate_freestyle_name(), self.item_type.FREESTYLE)
        item_page = open_page(BaseConfigurationPage, self.endpoints.JOB_CONFIGURE_URL(job_name))
        item_page.disable_project()
        item_page.save_configuration()
        text = item_page.check_message_disable()
        item_page.assert_disable_text(text)

