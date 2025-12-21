import time
import random


def test_tc_06_003_01(page):
    page.goto("/")

    name_item = f"Pipeline project-{random.randint(1, 9999)}"
    description_text = f"Here is a description of {name_item}"

    """Locators"""
    new_item_loc = "a[href='/view/all/newJob']"
    pipeline_multi_loc = "Multibranch pipeline"
    field_name_loc = "input[name='name']"
    button_ok_loc = "button[id='ok-button']"
    description_loc = "textarea[name='_.description']"
    preview_loc = "a[class='textarea-show-preview']"
    preview_field_loc = "div.textarea-preview"
    button_save_loc= "button[name='Submit']"
    status_text_loc= "[id='view-message']"

    "Preconditions"
    page.locator(new_item_loc).click()
    page.locator(field_name_loc).fill(name_item)
    page.get_by_text(pipeline_multi_loc).click()
    page.locator(button_ok_loc).click()

    "Testing"
    page.locator(description_loc).fill(description_text)
    page.locator(preview_loc).click()
    page.locator(preview_field_loc).wait_for(state="visible")
    assert page.locator(preview_field_loc).text_content() == description_text
    page.locator(button_save_loc).click()

    assert page.locator(status_text_loc).text_content() == description_text
    assert page.get_by_text("Add description").is_visible()






