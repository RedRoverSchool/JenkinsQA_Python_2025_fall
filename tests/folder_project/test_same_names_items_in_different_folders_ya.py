

def test_tc_01_002_07_same_names_items_in_different_folders(page):
    # Предусловия
    for folder in ["Folder_1", "Folder_2"]:
        page.goto("/view/all/newJob")
        page.fill("#name", folder)
        page.locator("li.com_cloudbees_hudson_plugins_folder_Folder").click()
        page.locator("#ok-button").click()

    page.goto("/job/Folder_1/newJob")
    page.fill("#name", "MyProject")
    page.locator("li.hudson_model_FreeStyleProject").click()
    page.locator("#ok-button").click()

    # Основной тест
    page.goto("/job/Folder_2/newJob")
    page.fill("#name", "MyProject")
    page.locator("li.hudson_model_FreeStyleProject").click()
    page.locator("#ok-button").click()

    assert "/job/Folder_2/job/MyProject/" in page.url

    for folder in ["Folder_1", "Folder_2"]:
        page.goto(f"/job/{folder}/delete")
        page.locator("button[name='Submit']").click()