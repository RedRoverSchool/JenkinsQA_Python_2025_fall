import random
from playwright.sync_api import Page, expect


def test_add_description_option_displayed(page: Page):
    """
    Test that 'Add description' option is displayed and functional
    when a folder has no existing description.
    """
    page.goto("/")

    new_folder_name = f"Test_folder_{random.randint(0, 999999)}"

    page.get_by_role("link", name="New Item").click()
    page.locator("input#name").fill(new_folder_name)
    page.get_by_text("Folder", exact=True).click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("button", name="Save").click()

    page.goto(f"/job/{new_folder_name}/")
    page.wait_for_load_state("domcontentloaded")

    description_text_locator = "div#description div"
    folder_heading = page.get_by_role("heading", name=new_folder_name, exact=True)
    expect(folder_heading).to_be_visible()

    description_locator = page.locator(description_text_locator)
    if description_locator.count() > 0:
        description_text = description_locator.first.text_content()
        if description_text:
            description_text = description_text.strip()
            assert description_text == "", f"Expected no description, found some : '{description_text}'"

    add_description_link = page.get_by_role("link", name="Add description")
    expect(add_description_link).to_be_visible()
    expect(add_description_link).to_be_enabled()

    edit_description_link = page.get_by_role("link", name="Edit description")
    expect(edit_description_link).not_to_be_visible()

    add_description_link.click()
    page.wait_for_timeout(1000)

    description_textarea = page.locator("textarea[name='description']")
    expect(description_textarea).to_be_visible()
    expect(description_textarea).to_be_editable()

    test_input = "Test description has now input"
    description_textarea.fill(test_input)
    actual_value = description_textarea.input_value()

    assert actual_value == test_input, f"Expected textarea value '{test_input}', but got '{actual_value}'"