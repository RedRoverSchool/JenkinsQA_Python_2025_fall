import random

from playwright.sync_api import expect


def test_TC_01_002_02(page):
    page.goto("/")

    new_folder_name = f"Test_folder_{random.randint(0, 999999)}"
    folder_name = new_folder_name

    new_item_link_loc = "a[href='/view/all/newJob']"

    item_name_field_loc = "input[id='name']"
    item_type_text = "Folder"
    ok_btn_loc = "button[id='ok-button']"
    save_btn_loc = "button[name='Submit']"
    home_page_loc = "a[href='/']"
    error_message_loc = "div[id='itemname-invalid']"

    page.locator(new_item_link_loc).click()
    page.locator(item_name_field_loc).fill(new_folder_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()

    page.locator(save_btn_loc).click()

    page.locator(home_page_loc).click()
    page.locator(new_item_link_loc).click()
    page.locator(item_name_field_loc).fill(folder_name)

    expect(page.locator(error_message_loc)).to_have_text(f"» A job already exists with the name ‘{folder_name}’")