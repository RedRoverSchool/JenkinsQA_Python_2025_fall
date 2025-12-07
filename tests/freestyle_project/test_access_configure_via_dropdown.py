from playwright.sync_api import expect
import random


def test_tc_02_001_001_access_configure_via_dropdown(page):
    freestyle_project_name = f"Freestyle_{random.randint(1, 999999)}"

    new_item_btn_loc = "a[href='/view/all/newJob']"
    item_name_field = "#name"
    freestyle_item_type_loc = "//span[text()='Freestyle project']"
    ok_btn_loc = "button#ok-button"
    save_btn_loc = "button[name='Submit']"
    home_icon_loc = "#jenkins-head-icon"
    dropdown_arrow_loc = (
        f"a[href='job/{freestyle_project_name}/'] button.jenkins-menu-dropdown-chevron"
    )
    page.goto("/")
    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field).fill(freestyle_project_name)
    page.locator(freestyle_item_type_loc).click()
    page.locator(ok_btn_loc).click()
    page.locator(save_btn_loc).click()
    page.locator(home_icon_loc).click()
    page.locator(dropdown_arrow_loc).click(force=True)
    page.locator("a:has-text('Configure')").click()

    expect(page).to_have_url(f"/job/{freestyle_project_name}/configure")
