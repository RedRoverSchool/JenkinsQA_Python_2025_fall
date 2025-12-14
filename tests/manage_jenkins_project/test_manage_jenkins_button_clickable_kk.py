from conftest import BASE_URL


def test_manage_jenkins_button_clickable(page):
    page.goto("/")

    manage_jenkins_link_locator = "a[id='root-action-ManageJenkinsAction']"

    page.locator(manage_jenkins_link_locator).click()

    assert page.url == f"{BASE_URL}/manage/"