def test_manage_jenkins_button_availability(page):
    page.goto("/")

    assert page.locator("a[id='root-action-ManageJenkinsAction']")