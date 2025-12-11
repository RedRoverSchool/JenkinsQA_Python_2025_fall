

def test_unique_item_name_constraint(page):
    """Предусловия"""
    page.goto("/")
    page.locator("a[href='/view/all/newJob']").click()
    page.locator("#name").fill("Autotests")
    page.locator("li.com_cloudbees_hudson_plugins_folder_Folder").click()
    page.locator("button[id='ok-button']").click()
    page.locator("#jenkins-head-icon").click()
    page.locator("a.jenkins-table__link.model-link.inside[href='job/Autotests/']").click()
    page.locator("a[href='/job/Autotests/newJob']").click()
    page.locator("#name").fill("Test_Project")
    page.locator(".hudson_model_FreeStyleProject").click()
    page.locator("button[id='ok-button']").click()
    
    folder_name = "Autotests"
    existing_project = "Test_Project"

    page.goto(f"/job/{folder_name}")
    page.wait_for_selector("a[href='/job/Autotests/newJob']", timeout=60000)
    page.click("a[href='/job/Autotests/newJob']")

    page.fill("#name", existing_project)
    page.wait_for_timeout(1000)

    error_locator = page.locator("#itemname-invalid")

    assert error_locator.is_visible()
    actual_error_text = error_locator.inner_text()
    print(f"Текст ошибки: '{actual_error_text}'")
