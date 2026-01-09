import allure

from data.enums import ItemType
from data.endpoints import Endpoints
from pages.base_configuration_page import BaseConfigurationPage
from pages.base_project_page import BaseProjectPage
from pages.jenkins_base_page import JenkinsBasePage
from utils.generators.project_generator import ProjectGenerator

@allure.epic("Pipeline")
@allure.feature("Essential features in pipeline")
class TestPipeline:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    item_type = ItemType

    @allure.story("Create pipeline")
    def test_create_pipeline_project(self, create_job, open_page):
        job_name = create_job(self.generator.generate_folder_name(), ItemType.PIPELINE)
        folder_project = open_page(JenkinsBasePage, self.endpoints.VIEW_ALL_PAGE_URL)
        name = folder_project.get_created_job_by_name(job_name)

        assert name == job_name

    @allure.story("Create pipeline with description")
    def test_tc_03_002_01_create_project_with_description(self, page, create_job, open_page):
        """Add description to the new project"""
        description_text = self.generator.generate_random_text(10) # generate random text for description
        job_name = create_job(self.generator.generate_folder_name(), self.item_type.PIPELINE)  # create job
        pipeline_page = open_page(BaseConfigurationPage,
                                  self.endpoints.JOB_CONFIGURE_URL(job_name))  # open configuration page of created job
        pipeline_page.set_or_change_description(description_text)  # add description to the job
        pipeline_page.save_configuration()  # save configuration
        pipeline_status_page = open_page(BaseProjectPage, self.endpoints.JOB_STATUS_PAGE_URL(
            job_name))  # open status(project) page of job
        text = pipeline_status_page.description_text(description_text)  # read inner text from locator _description

        assert text == description_text

    @allure.story("Add description to the existing pipeline job")
    def test_rf_tc_03_002_02_add_description(self, create_job, open_page):
        """Add description to the existing project"""
        description_text = self.generator.generate_random_text(10)  # generate random text for description
        job_name = create_job(self.generator.generate_folder_name(), self.item_type.PIPELINE)  # created pipeline job
        pipeline_jenkins_page = open_page(JenkinsBasePage,
                                          self.endpoints.VIEW_ALL_PAGE_URL)  # open dashboard with all pipeline
        job_name_from_dashboard = pipeline_jenkins_page.get_created_job_by_name(job_name)  # find created job by name
        pipeline_page = open_page(BaseConfigurationPage, self.endpoints.JOB_CONFIGURE_URL(
            job_name_from_dashboard))  # open configuration page of created job
        pipeline_page.set_or_change_description(description_text)  # add description to the job
        pipeline_page.save_configuration()  # save configuration
        pipeline_status_page = open_page(BaseProjectPage, self.endpoints.JOB_STATUS_PAGE_URL(
            job_name))  # open status(project) page of job
        description = pipeline_status_page.description_text(
            description_text)  # read inner text from locator _description

        assert description == description_text