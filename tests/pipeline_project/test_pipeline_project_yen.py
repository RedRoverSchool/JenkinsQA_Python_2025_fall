import random

from playwright.sync_api import expect

project_name = f"PipelineProject_{random.randint(1, 100)}"


def test_create_pipeline_project(page, delete_project):
    new_job_link_loc = "//a[@href='newJob']"
    item_name_field_loc = "//input[@id='name']"
    pipeline_link_loc = "//div/label/span[text()='Pipeline']"
    ok_button_loc = "//button[@id='ok-button']"

    page.goto("/")
    page.locator(new_job_link_loc).click()
    page.locator(item_name_field_loc).fill(project_name)
    page.locator(pipeline_link_loc).click()
    page.locator(ok_button_loc).click()

    page.get_by_role("link", name="Jenkins", exact=True).click()

    expect(page.get_by_role("link", name=project_name, exact=True)).to_be_visible()