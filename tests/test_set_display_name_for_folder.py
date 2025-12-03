from playwright.sync_api import expect
import random


def test_set_display_name_for_folder(page):
    page.goto("/")

    new_item_link_loc = "a[href='newJob']"
    ok_button_loc = "button[id='ok-button']"
    save_button_loc = "button[name='Submit']"
    logo_jenkins_loc = "a[href='/']"
    display_name_input_loc = "input[name='_.displayNameOrNull']"

    project_folder_name = f"ProjectFolder_{random.randint(0, 99999)}"
    item_type_text = "Folder"
    display_name = "The Displayed Name of the Folder"
    error_message = "Display Name was not found in Configuration."

    page.locator(new_item_link_loc).click()
    page.fill("input#name", project_folder_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_button_loc).click()

    expect(page.locator("#main-panel")).to_be_visible()

    page.locator(display_name_input_loc).fill(display_name)
    page.locator(save_button_loc).click()

    expect(page.locator("h1")).to_contain_text(display_name)
    page.reload()
    expect(page.locator("h1")).to_contain_text(display_name)

    page.locator(logo_jenkins_loc).click()
    page.goto(f"/job/{project_folder_name}/")
    expect(page.locator("h1")).to_contain_text(display_name)

    page.goto(f"/job/{project_folder_name}/configure")
    page.wait_for_load_state("domcontentloaded")

    config_display_name = page.locator(display_name_input_loc).input_value()
    assert config_display_name == display_name, error_message
