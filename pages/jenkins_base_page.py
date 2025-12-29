from pages.base_page import BasePage
from locators.base_locators import BaseLocators


class JenkinsBasePage(BasePage):

    def get_created_job_by_name(self, job_name):
        return self.get_text(BaseLocators.NAME_OF_CREATED_PROJECT(job_name))
