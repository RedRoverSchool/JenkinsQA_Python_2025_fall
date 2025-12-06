from playwright.sync_api import expect
import random
import re


def test_tc_02_001_005_re_enable_project_by_toggle(page):
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
    enabled_message_text = "Enabled"

    page.goto("/")
    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field).fill(freestyle_project_name)
    page.locator(freestyle_item_type_loc).click()
    page.locator(ok_btn_loc).click()
    page.locator(save_btn_loc).click()

    # === Disable project first (to satisfy test Preconditions) ===
    page.locator(home_icon_loc).click()
    page.get_by_role("link", name=freestyle_project_name, exact=True).click()
    page.locator(configure_button_loc).click()
    expect(page).to_have_url(re.compile(r"/configure/?$"))
    page.locator(toggle_label_loc).click()
    page.locator(save_btn_loc).click()
    expect(page.get_by_text(disabled_banner_text, exact=False)).to_be_visible()

    #  MAIN TEST FLOW: RE-ENABLE PROJECT
    page.locator(configure_button_loc).click()
    page.locator(toggle_label_loc).click()  # Enable toggle (switch ON)

    expect(page.get_by_text(enabled_message_text, exact=False)).to_be_visible()
    page.locator(save_btn_loc).click()
    # Expected Result: No Disabled status on project page ===
    expect(page.get_by_text(disabled_banner_text, exact=False)).not_to_be_visible()
    expect(page.locator("//svg[@title='Disabled']")).not_to_be_visible()
