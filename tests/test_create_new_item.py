import time

from playwright.sync_api import expect


def test_create_new_item(page):
    page.goto("/")

    page.locator("a[it='hudson.model.Hudson@16bae93d']").click()

    pipeline_name = "Pipeline1"
    page.locator("input[id='name']").fill(pipeline_name)

    page.locator("li.org_jenkinsci_plugins_workflow_job_WorkflowJob").click()

    page.locator("#ok-button").click()

    page.locator("a[href='/']").click()

    expect(page.get_by_role("link", name=pipeline_name, exact=True)).to_be_visible()