import random

import pytest
from playwright.sync_api import expect

from data.enums import ItemType
from data.endpoints import Endpoints
from pages.base_configuration_page import BaseConfigurationPage
from pages.base_project_page import BaseProjectPage
from pages.jenkins_base_page import JenkinsBasePage
from utils.generators.project_generator import ProjectGenerator

project_name = f"PipelineProject_{random.randint(1, 100)}"


class TestPipeline:
    generator = ProjectGenerator()
    endpoints = Endpoints()
    item_type = ItemType

    def test_create_pipeline_project(self, create_job, open_page):
        job_name = create_job(self.generator.generate_folder_name(), ItemType.PIPELINE)
        folder_project = open_page(JenkinsBasePage, self.endpoints.VIEW_ALL_PAGE_URL)
        name = folder_project.get_created_job_by_name(job_name)

        assert name == job_name

    @pytest.mark.skip
    def test_add_description_pipeline_project(self, page, delete_project):
        description_text = "Description pipeline project"
        new_job_link_loc = "//a[@href='newJob']"
        item_name_field_loc = "//input[@id='name']"
        pipeline_link_loc = "//div/label/span[text()='Pipeline']"
        ok_button_loc = "//button[@id='ok-button']"
        description_text_loc = "//textarea[@name='description']"
        submit_button_loc = "//button[@name='Submit']"
        description_content_text = "#description-content"

        page.goto("/")
        page.locator(new_job_link_loc).click()
        page.locator(item_name_field_loc).fill(project_name)
        page.locator(pipeline_link_loc).click()
        page.locator(ok_button_loc).click()
        page.locator(description_text_loc).fill(description_text)
        page.locator(submit_button_loc).click()

        expect(page.locator(description_content_text)).to_have_text(description_text)

    def test_rf_tc_03_002_02_add_description(self, create_job, open_page):
        """Add description to the project"""
        random_text = self.generator.generate_random_text(10)
        job_name = create_job(self.generator.generate_freestyle_name(), self.item_type.FREESTYLE)
        pipeline_page = open_page(BaseConfigurationPage, self.endpoints.JOB_CONFIGURE_URL(job_name))
        pipeline_page.set_or_change_description(random_text)
        pipeline_page.save_configuration()
        pipeline_status_page = open_page(BaseProjectPage, self.endpoints.JOB_STATUS_PAGE_URL(job_name))
        text = pipeline_status_page.description_text(random_text)

        assert text == random_text