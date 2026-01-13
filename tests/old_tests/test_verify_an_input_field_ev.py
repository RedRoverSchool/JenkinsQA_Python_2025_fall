import time
from playwright.sync_api import expect

def test_verify_an_input_field(page):
    page.goto('/')
    time.sleep(2)

    page.locator("a[href='/view/all/newJob']").click()

    label = page.locator('//label[@for="name"]')

    expect(label).to_have_text("Enter an item name")



