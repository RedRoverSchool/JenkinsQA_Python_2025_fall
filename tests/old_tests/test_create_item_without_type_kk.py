import random
from playwright.sync_api import expect


def test_create_item_without_type(page):
    page.goto("/")

    new_item_link_loc = "a[href='/view/all/newJob']"

    item_name_field_loc = "input[id='name']"
    ok_btn_loc = "button[id='ok-button']"

    page.locator(new_item_link_loc).click()
    page.locator(item_name_field_loc).fill(f"Test_folder_{random.randint(0, 999999)}")

    expect(page.locator(ok_btn_loc)).to_be_disabled()