import time
from faker import Faker
from playwright.sync_api import expect

fake = Faker()
random_name = fake.name()
def test_entire_list_visible(page):
    page.goto('/')

    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//input[@id="name"]').fill(random_name)
    page.locator('//li[@class="com_cloudbees_hudson_plugins_folder_Folder"]').click()
    page.locator('//button[@id="ok-button"]').click()
    configuration_page = page.locator('//span[contains(text(), "Configuration")]')
    expect(configuration_page).to_have_text("Configuration")
