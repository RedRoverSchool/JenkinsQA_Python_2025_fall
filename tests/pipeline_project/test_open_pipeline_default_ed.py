import random

from playwright.sync_api import expect

project_name = f"PipelineProject_{random.randint(1, 100)}"


def test_open_pipeline_default(page,delete_jobs_after_all_tests):
    new_job_link_loc = "//a[@href='newJob']"
    item_name_field_loc = "//input[@id='name']"
    pipeline_link_loc = "//div/label/span[text()='Pipeline']"
    ok_button_loc = "//button[@id='ok-button']"
    active_link = "#tasks a.task-link--active"

    page.goto("/")
    page.locator(new_job_link_loc).click()
    page.locator(item_name_field_loc).fill(project_name)
    page.locator(pipeline_link_loc).click()
    page.locator(ok_button_loc).click()

    page.get_by_role("link", name="Jenkins", exact=True).click()
    page.get_by_role("link", name=project_name, exact=True).click()

    expect(page.locator(active_link)).to_have_text("Status")

