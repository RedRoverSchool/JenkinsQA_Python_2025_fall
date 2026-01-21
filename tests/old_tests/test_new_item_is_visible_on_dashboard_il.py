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

    item_span = page.locator(f"//span[text()='{item_name}']")
    expect(item_span).to_be_visible()

