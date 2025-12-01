import random

from playwright.sync_api import expect


def test_TC_01_002_01(page):
    page.goto("/")

    new_folder_name = f"Test_folder_{random.randint(0, 999999)}"

    new_item_btn_loc = "a[href='/view/all/newJob']"

    item_name_field_loc = "input[class='jenkins-input']"
    item_type_text = "Folder"
    ok_btn_loc = "button[id='ok-button']"
    save_btn_loc = "button[name='Submit']"
    folder_title_loc = "h1.job-index-headline"


    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field_loc).fill(new_folder_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()

    page.locator(save_btn_loc).click()

    folder_title = page.locator(folder_title_loc)
    expect(folder_title).to_have_text(new_folder_name)











