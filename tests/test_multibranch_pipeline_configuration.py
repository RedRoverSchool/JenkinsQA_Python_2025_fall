import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="function")
def create_multibranch_pipeline(page):
    pipeline_name = "test-multibranch-pipeline"

    # Open New Item page
    page.goto("/view/all/newJob")

    # Enter pipeline name
    page.fill("input#name", pipeline_name)

    # Select Multibranch Pipeline
    page.click("label:has-text('Multibranch Pipeline')")

    # Click OK
    page.click("button#ok-button")

    # We are on Configure page now — just save
    page.click("button[name='Submit']")

    # Verify pipeline page is opened
    expect(page).to_have_url(f"/job/{pipeline_name}/")

    return pipeline_name

def test_multibranch_pipeline_change_description(page):
    pipeline_name = "test-multibranch-pipeline"
    description_text = "This is a test description for multibranch pipeline"

    # Step 1: Open Multibranch Pipeline Configure page
    page.goto(f"/job/{pipeline_name}/configure")

    # Step 2: Add description
    page.fill("textarea[name='description']", description_text)

    # Step 3: Click "Preview"
    page.click("button:has-text('Preview')")

    # Step 4: Click "Save"
    page.click("button[name='Submit']")

    # Step 5: Verify description is shown on pipeline page
    page.goto(f"/job/{pipeline_name}/")
    expect(page.locator("#description")).to_have_text(description_text)
