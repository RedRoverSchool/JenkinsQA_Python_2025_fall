import random
from playwright.sync_api import expect



def test_delete_folder(page):
    page.goto("/")
    created_folder_name = f"TestFolder_{random.randint(0, 100000000)}"
    new_item_btn_loc = "a[href='/view/all/newJob']"
    item_name_field_loc = "input[class='jenkins-input']"
    folder_item_type_text = "Folder"
    folder_name_text = f"{created_folder_name}"
    ok_btn_loc = "button[id='ok-button']"
    dashboard_page_loc = "span[class='jenkins-mobile-hide']"
    delete_folder_btn_loc = "button[href='/job/{created_folder_name}/doDelete']"
    confirm_deletion_btn_loc = "button[data-id='ok']"
    drop_down_btn_loc = f"button[data-href*='job/{created_folder_name}/']"
    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field_loc).fill(created_folder_name)
    page.get_by_text(folder_item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()
    page.locator(dashboard_page_loc).click()
    page.locator(drop_down_btn_loc).click()
    page.get_by_text("Delete Folder", exact=True).click()
    page.locator(confirm_deletion_btn_loc).click()
    locator = page.locator(created_folder_name)
    assert locator.count() == 0