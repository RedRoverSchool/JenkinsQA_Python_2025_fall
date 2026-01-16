from playwright.sync_api import expect


def test_tc_01_001_04(page):

    page.goto("/")

    # Locators
    new_item_btn_loc = "a[href='/view/all/newJob']"
    item_type_text_freestyle_project = "Freestyle project"
    item_type_text_pipeline = "Pipeline"
    item_type_text_multi_configuration_project = "Multi-configuration project"
    item_type_text_folder = "Folder"
    item_type_text_multibranch_pipeline = "Multibranch Pipeline"
    item_type_text_organization_folder = "Organization Folder"
    ok_btn_loc = "button[id='ok-button']"
    validation_message = "#itemname-required"

    page.locator(new_item_btn_loc).click()

    page.get_by_text(item_type_text_freestyle_project, exact=True).click()
    expect(page.locator(validation_message)).to_be_visible()
    expect(page.locator(ok_btn_loc)).to_be_disabled()


    page.get_by_text(item_type_text_pipeline, exact=True).click()
    expect(page.locator(validation_message)).to_be_visible()
    expect(page.locator(ok_btn_loc)).to_be_disabled()


    page.get_by_text(item_type_text_multi_configuration_project, exact=True).click()
    expect(page.locator(validation_message)).to_be_visible()
    expect(page.locator(ok_btn_loc)).to_be_disabled()


    page.get_by_text(item_type_text_folder, exact=True).click()
    expect(page.locator(validation_message)).to_be_visible()
    expect(page.locator(ok_btn_loc)).to_be_disabled()


    page.get_by_text(item_type_text_multibranch_pipeline, exact=True).click()
    expect(page.locator(validation_message)).to_be_visible()
    expect(page.locator(ok_btn_loc)).to_be_disabled()


    page.get_by_text(item_type_text_organization_folder, exact=True).click()
    expect(page.locator(validation_message)).to_be_visible()
    expect(page.locator(ok_btn_loc)).to_be_disabled()