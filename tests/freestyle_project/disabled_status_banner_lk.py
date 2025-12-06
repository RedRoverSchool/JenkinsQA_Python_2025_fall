from playwright.sync_api import expect
import random
import re


def test_tc_02_001_004_clickJenkinsLogo_toggleDisable(page):
    freestyle_project_name = f"Freestyle_{random.randint(1, 999999)}"

    new_item_btn_loc = "a[href='/view/all/newJob']"
    item_name_field = "#name"
    freestyle_item_type_loc = "//span[text()='Freestyle project']"
    ok_btn_loc = "button#ok-button"
    save_btn_loc = "button[name='Submit']"
    home_icon_loc = "#jenkins-head-icon"
    configure_button_loc = "a[href$='configure']"
    toggle_label_loc = "label[for='enable-disable-project']"

    disabled_banner_text = "This project is currently disabled"

    page.goto("/")
    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field).fill(freestyle_project_name)
    page.locator(freestyle_item_type_loc).click()
    page.locator(ok_btn_loc).click()
    page.locator(save_btn_loc).click()
    page.locator(home_icon_loc).click()
    page.get_by_role("link", name=freestyle_project_name, exact=True).click()
    page.locator(configure_button_loc).click()
    expect(page).to_have_url(re.compile(r"/configure/?$"))
    page.locator(toggle_label_loc).click()
    page.locator(save_btn_loc).click()
    page.locator(home_icon_loc).click()
    page.get_by_role("link", name=freestyle_project_name, exact=True).click()

    expect(page.get_by_text(disabled_banner_text, exact=False)).to_be_visible()  # banner message is visible
