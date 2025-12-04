

def test_verify_visual_selection(page):

    page.goto("/view/all/newJob")
    page.fill("#name", "Test_Pipeline")


    pipeline_locator = page.locator("li.org_jenkinsci_plugins_workflow_job_WorkflowJob")
    pipeline_locator.click()

    assert "active" in pipeline_locator.get_attribute("class")

    ok_button = page.locator("button#ok-button")
    assert ok_button.is_enabled()


