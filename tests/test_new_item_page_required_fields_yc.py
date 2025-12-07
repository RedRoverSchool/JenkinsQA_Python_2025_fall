from playwright.sync_api import expect


def test_tc_01_001_14(page):

    page.goto("/")

    # Locators
    new_item_btn_loc = "a[href='/view/all/newJob']"
    item_name_field = "#name"
    item_type_text_freestyle_project = "Freestyle project"
    item_type_text_pipeline = "Pipeline"
    item_type_text_multi_configuration_project = "Multi-configuration project"
    item_type_text_folder = "Folder"
    item_type_text_multibranch_pipeline = "Multibranch Pipeline"
    item_type_text_organization_folder = "Organization Folder"
    copy_from_field = "#from"
    ok_btn_loc = "button[id='ok-button']"

    # Test
    page.locator(new_item_btn_loc).click()
    assert page.url.endswith("/view/all/newJob")

    expect(page.locator(item_name_field)).to_be_visible()
    expect(page.get_by_text(item_type_text_freestyle_project, exact=True)).to_be_visible()
    expect(page.get_by_text(item_type_text_pipeline, exact=True)).to_be_visible()
    expect(page.get_by_text(item_type_text_multi_configuration_project, exact=True)).to_be_visible()
    expect(page.get_by_text(item_type_text_folder, exact=True)).to_be_visible()
    expect(page.get_by_text(item_type_text_multibranch_pipeline, exact=True)).to_be_visible()
    expect(page.get_by_text(item_type_text_organization_folder, exact=True)).to_be_visible()

    copy_from = page.locator(copy_from_field)
    copy_from.scroll_into_view_if_needed()
    expect(copy_from).to_be_visible()

    expect(page.locator(ok_btn_loc)).to_be_visible()


















