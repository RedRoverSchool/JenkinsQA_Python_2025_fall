import random

from playwright.sync_api import expect

project_name = f"PipelineProject_{random.randint(1, 100)}"


def test_create_pipeline_project(page):
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

def test_add_description_pipeline_project(page):
    description_text = "Description pipeline project"
    new_job_link_loc = "//a[@href='newJob']"
    item_name_field_loc = "//input[@id='name']"
    pipeline_link_loc = "//div/label/span[text()='Pipeline']"
    ok_button_loc = "//button[@id='ok-button']"
    description_text_loc = "//textarea[@name='description']"
    submit_button_loc= "//button[@name='Submit']"
    description_content_text = "#description-content"

    page.goto("/")
    page.locator(new_job_link_loc).click()
    page.locator(item_name_field_loc).fill(project_name)
    page.locator(pipeline_link_loc).click()
    page.locator(ok_button_loc).click()
    page.locator(description_text_loc).fill(description_text)
    page.locator(submit_button_loc).click()

    expect(page.locator(description_content_text)).to_have_text(description_text)