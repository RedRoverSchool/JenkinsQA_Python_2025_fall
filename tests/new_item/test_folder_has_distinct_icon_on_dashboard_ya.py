import allure
from pages.base_page import BasePage
from utils.generators.project_generator import ProjectGenerator
from locators.dashboard_locators import DashboardLocators


@allure.title("TC_01.002.05 | New Item > Folder > Verify folder has a distinct icon on the dashboard")
def test_tc_01_002_05_folder_has_distinct_icon(page, create_job, open_page):

    folder_name = ProjectGenerator.generate_folder_name()
    create_job(folder_name, job_type="folder")
    base_page = open_page(BasePage, "/")

    locator = DashboardLocators.folder_with_icon(folder_name)
    assert base_page.page.locator(locator).is_visible()






