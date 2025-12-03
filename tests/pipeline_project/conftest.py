import pytest

from tests.pipeline_project import test_pipeline_project_yen


@pytest.fixture
def delete_project(page):
    yield page
    page.get_by_role("link", name=test_pipeline_project_yen.project_name, exact=True).click()
    page.locator("//a[@data-title='Delete Pipeline']").click()
    page.get_by_role("button", name="Yes", exact=True).click()