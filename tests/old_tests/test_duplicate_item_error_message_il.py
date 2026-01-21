from faker import Faker
from playwright.sync_api import expect

fake = Faker()

def test_duplicate_item_error_message(page):
    item_name = fake.user_name()

    page.goto('/')

    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//input[@id="name"]').fill(item_name)
    freestyle = page.locator('//li[contains(@class,"hudson_model_FreeStyleProject")]')
    expect(freestyle).to_be_visible()
    freestyle.click()

    page.locator('//button[@id="ok-button"]').click()

    page.get_by_role("link", name="Jenkins", exact=True).click()
    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//input[@id="name"]').fill(item_name)


    error_message = page.locator('//div[@id="itemname-invalid"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("A job already exists with the name")
