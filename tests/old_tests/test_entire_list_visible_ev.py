import time

from playwright.sync_api import expect

def test_entire_list_visible(page):
    page.goto('/')
    time.sleep(2)

    page.locator("a[href='/view/all/newJob']").click()

    label1 = page.locator('//label/span[contains(@class, "label") and contains(text(), "Freestyle project")]')
    expect(label1).to_have_text("Freestyle project")

    label2 = page.locator('(//span[contains(text(), "Pipeline")])[1]')
    expect(label2).to_have_text("Pipeline")

    label3 = page.locator('(//span[contains(text(), "Multi-configuration project")])')
    expect(label3).to_have_text("Multi-configuration project")

    label4 = page.locator('(//span[contains(text(), "Folder")])[1]')
    expect(label4).to_have_text("Folder")

    label5 = page.locator('(//span[contains(text(), "Multibranch Pipeline")])')
    expect(label5).to_have_text("Multibranch Pipeline")

    label6 = page.locator('(//span[contains(text(), "Organization Folder")])')
    expect(label6).to_have_text("Organization Folder")




