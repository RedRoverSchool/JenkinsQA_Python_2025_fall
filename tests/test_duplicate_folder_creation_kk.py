import random


def test_duplicate_folder_creation(page):
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

    assert page.locator(error_message_loc) is not None