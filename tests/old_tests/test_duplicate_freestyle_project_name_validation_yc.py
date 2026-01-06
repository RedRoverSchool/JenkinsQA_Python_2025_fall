from playwright.sync_api import expect
import random


def test_tc_01_001_03(page):

    page.goto("/")

    # Locators
    new_item_btn_loc = "a[href='/view/all/newJob']"
    item_name_field = "#name"
    new_freestyle_project_name = f"Test_freestyle_project_{random.randint(0, 999999)}"
    item_type_text_freestyle_project = "Freestyle project"
    ok_btn_loc = "button[id='ok-button']"
    duplicate_validation_message = "#itemname-invalid"
    save_btn_loc = "button[name='Submit']"
    home_page_loc = "#jenkins-head-icon"

    # Preconditions (creating new Freestyle project item)
    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field).fill(new_freestyle_project_name)
    page.get_by_text(item_type_text_freestyle_project, exact=True).click()
    page.locator(ok_btn_loc).click()

    page.locator(save_btn_loc).click()

    page.locator(home_page_loc).click()


    # Test
    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field).fill(new_freestyle_project_name)
    expect(page.locator(duplicate_validation_message)).to_be_visible()








