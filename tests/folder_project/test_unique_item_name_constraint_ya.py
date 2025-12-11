

def test_unique_item_name_constraint(page):

    folder_name = "Autotests"
    existing_project = "Test_Project"

    page.goto(f"/job/{folder_name}")
    page.click("a[href='/job/Autotests/newJob']")

    page.fill("#name", existing_project)
    page.wait_for_timeout(1000)

    error_locator = page.locator("#itemname-invalid")

    assert error_locator.is_visible()
    actual_error_text = error_locator.inner_text()
    print(f"Текст ошибки: '{actual_error_text}'")