# import os
# import pytest
# from playwright.sync_api import expect
# import random
# from conftest import BASE_URL
#
#
# @pytest.fixture
# def new_folder(page):
#     new_folder_name = f"Test_folder_{random.randint(0, 999999)}"
#
#     new_item_link_loc = "a[href='/view/all/newJob']"
#     item_name_field_loc = "input[class='jenkins-input']"
#     item_type_text = "Folder"
#     ok_btn_loc = "button[id='ok-button']"
#     save_btn_loc = "button[name='Submit']"
#     folder_title_loc = "h1.job-index-headline"
#
#     page.goto("/")
#     page.locator(new_item_link_loc).click()
#     page.locator(item_name_field_loc).fill(new_folder_name)
#     page.get_by_text(item_type_text, exact=True).click()
#     page.locator(ok_btn_loc).click()
#     page.locator(save_btn_loc).click()
#
#     folder_title = page.locator(folder_title_loc)
#     expect(folder_title).to_have_text(new_folder_name)
#
#     return new_folder_name
#
#
# @pytest.fixture
# def new_view(page, new_folder):
#
#     new_name = f"New_name_{random.randint(0, 999999)}"
#
#     new_view_link_loc = page.locator(f"a[href='/job/{new_folder}/newView']")
#     view_name_input_loc = page.locator("input[name='name']")
#     global_view_type_loc = page.get_by_text("Include a global view")
#     create_btn_loc = page.get_by_role("button", name="Create")
#     save_btn_loc = page.get_by_role("button", name="Save")
#
#     new_view_link_loc.click()
#
#     view_name_input_loc.fill(new_name)
#
#     global_view_type_loc.check()
#
#     create_btn_loc.click()
#     expected_url = f"{BASE_URL}/job/{new_folder}/view/{new_name}/configure"
#     expect(page).to_have_url(expected_url)
#
#     save_btn_loc.click()
#     expect(page).to_have_url(f"{BASE_URL}/job/{new_folder}/view/{new_name}/?")
#
#     expect(page.get_by_text(new_name)).to_be_visible()
#
#     return new_name
