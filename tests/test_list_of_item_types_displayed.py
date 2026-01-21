from playwright.sync_api import expect

def test_list_of_item_types_displayed(page):
    page.goto('/')

    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//a[@href="/view/all/newJob"]')

    item_name_freestyle_project = page.locator('//span[contains(text(),"Freestyle project")]')
    expect(item_name_freestyle_project).to_have_text("Freestyle project")

    item_name_pipeline = page.locator('(//span[contains(text(),"Pipeline")])[1]')
    expect(item_name_pipeline).to_have_text("Pipeline")

    item_name_multi_configuration_project = page.locator('//span[contains(text(),"Multi-configuration project")]')
    expect(item_name_multi_configuration_project).to_have_text("Multi-configuration project")

    item_name_folder = page.locator('//span[normalize-space(text())="Folder"]')
    expect(item_name_folder).to_have_text("Folder")

    item_name_multibranch_pipeline = page.locator('//span[contains(text(),"Multibranch Pipeline")]')
    expect(item_name_multibranch_pipeline).to_have_text("Multibranch Pipeline")

    item_name_organization_folder = page.locator('//span[contains(text(),"Organization Folder")]')
    expect(item_name_organization_folder).to_have_text("Organization Folder")
