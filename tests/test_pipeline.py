 create_pipeline(page, name):
    """This function it`s not a test it`s function  just for create pipeline project without description,
    it`s necessary for next test cases"""

    # locators
    new_item_link_loc = "a[href='/view/all/newJob']"
    item_name_field_loc = "input[id='name']"
    ok_btn_loc = "button[id='ok-button']"
    submit_locator = "button[name='Submit']"
    dashboard_page_loc = "a[href='/']"

    # create job -> name
    page.goto("/")
    page.locator(new_item_link_loc).click()
    page.locator(item_name_field_loc).fill(name)
    page.get_by_text("Pipeline", exact=True).click()
    page.locator(ok_btn_loc).click()
    page.locator(submit_locator).click()
    page.locator(dashboard_page_loc).click()


def test_TC_03_002_02(page):
    """Add description to the project"""

    # Constants
    PIPELINE_NAME = "Pipeline_project"
    DESCRIPTION = "Lorem ipsum bla bla bla ..."

    # locators
    job_name = f"td a[href='job/{PIPELINE_NAME}/']"
    description_loc = "a[id='description-link']"
    textarea_loc = "textarea[name='description']"
    button_submit = "button[name='Submit']"
    description_content = "div[id='description-content']"

    # Calling method for create pipeline
    create_pipeline(page, PIPELINE_NAME)

    # Add description to the project PIPELINE_NAME
    page.goto("/")
    page.locator(job_name).click()
    page.locator(description_loc).click()
    page.locator(textarea_loc).fill(DESCRIPTION)
    page.locator(button_submit).click()
    description_text = page.locator(description_content).inner_text()

    assert description_text == DESCRIPTION
