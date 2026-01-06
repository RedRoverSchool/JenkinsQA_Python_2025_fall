from data.endpoints import Endpoints
from data.enums import ItemType
from pages.base_configuration_page import BaseConfigurationPage
from pages.base_project_page import BaseProjectPage
from utils.generators.project_generator import ProjectGenerator


class TestConfiguration:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    item_type = ItemType
    description_text = generator.generate_random_text(10) # generate random text for description


    def test_apply_configuration(self,create_job, open_page):
        '''TC_05.004.01 | Folder Configuration > Save or Apply> Apply configuration'''

        job_name = create_job(self.generator.generate_folder_name(), ItemType.FOLDER)
        configuration_page = open_page(BaseConfigurationPage, self.endpoints.JOB_CONFIGURE_URL(
            job_name))
        configuration_page.set_or_change_description(self.description_text)
        configuration_page.apply_changes()
        base_folder_page = open_page(BaseProjectPage, self.endpoints.JOB_STATUS_PAGE_URL(
            job_name))

        assert base_folder_page.description_text(self.description_text) == self.description_text