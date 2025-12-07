from playwright.sync_api import expect

def test_tc_01_002_05(page):
    page.goto("/")

    new_item_btn_loc = "a[href='/view/all/newJob']"
    page.locator(new_item_btn_loc).click()

    item_name_field = "#name"
    page.locator(item_name_field).fill("Autotests")

    folder_loc = "li.com_cloudbees_hudson_plugins_folder_Folder"
    page.locator(folder_loc).click()

    ok_btn_loc = "button[id='ok-button']"
    page.locator(ok_btn_loc).click()

    logo_jenkins_loc = "#jenkins-head-icon"
    page.locator(logo_jenkins_loc).click()

    # Test
    folder_icon = page.locator(".symbol-folder-outline")
    expect(folder_icon.first).to_be_visible()

    icon_class = folder_icon.first.get_attribute("class")
    assert "folder" in icon_class.lower(), f"Expected folder icon class, got: {icon_class}"





