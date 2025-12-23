from playwright.sync_api import expect


def test_create_item_with_empty_field(page):
    page.goto("/")

    page.locator("a[href='/view/all/newJob']").click()

    page.locator("#name").fill("")

    page.locator("li.org_jenkinsci_plugins_workflow_job_WorkflowJob").click()

    expect(page.locator("#ok-button")).to_be_disabled()

    expect(page.locator("#itemname-required")).to_contain_text(
        "This field cannot be empty, please enter a valid name"
    )