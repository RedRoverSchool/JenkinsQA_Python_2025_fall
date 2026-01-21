from playwright.sync_api import expect

def test_enter_an_item_name_field(page):
    page.goto('/')

    page.locator("a[href='/view/all/newJob']").click()

    page.locator('//a[@href="/view/all/newJob"]')

    item_name_input = page.locator('//input[@id="name"]')

    valid_names = [
        "Item1",
        "item_name",
        "ITEM_123",
        "itemName_2024"
    ]

    for name in valid_names:
        item_name_input.fill("")
        item_name_input.fill(name)

        expect(item_name_input).to_have_value(name)
