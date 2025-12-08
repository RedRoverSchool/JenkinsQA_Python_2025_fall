from playwright.sync_api import expect
def test_tc_01_002_08_create_new_folder_in_current_folder(page):
    page.goto("/")

    parent_folder_name = "parent_folder"
    child_folder_name = "child_folder"
    item_type_text = "Folder"

    new_item_link_loc = "a[href='/view/all/newJob']"
    item_name_field_loc = "input[class='jenkins-input']"
    ok_btn_loc = "button[id='ok-button']"
    save_btn_loc = "button[name='Submit']"
    logo_loc = 'img[id="jenkins-head-icon"]'
    parent_folder_row_loc = f"#job_{parent_folder_name}"
    child_folder_row_loc = f"#job_{child_folder_name}"
    projectstatus_row_loc = "#projectstatus tbody tr"

    page.locator(new_item_link_loc).click()
    page.locator(item_name_field_loc).fill(parent_folder_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()
    page.locator(save_btn_loc).click()
    page.get_by_text("New Item").click()
    page.locator(item_name_field_loc).fill(child_folder_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()
    page.locator(save_btn_loc).click()
    page.locator(logo_loc).click()

    parent_folder_row = page.locator(parent_folder_row_loc)

    expect(parent_folder_row).to_be_visible()
    expect(page.locator(projectstatus_row_loc)).to_have_count(1)

    page.get_by_role("link", name = parent_folder_name).click()
    child_folder_row = page.locator(child_folder_row_loc)

    expect(child_folder_row).to_be_visible()
