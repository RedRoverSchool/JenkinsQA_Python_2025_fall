import time
from playwright.sync_api import expect

def test_verify_an_input_field(page):
    page('/')
    time.sleep(2)

    page.locator("a[href='/view/all/newJob']").click()

    page.field('//label[@for="name"]')

    assert "Enter an item name"



