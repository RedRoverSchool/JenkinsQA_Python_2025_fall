import pytest

from tests.freestyle_project.freestyle_data import Freestyle


@pytest.fixture(scope="function")
def freestyle(page):
    page.goto("/")
    page.get_by_text("New Item").click()
    page.get_by_text("Enter an item name").fill(Freestyle.project_name)
    page.get_by_text(Freestyle.freestyle_type_text).click()
    page.get_by_text('OK').click()
    page.wait_for_url(f'/job/{Freestyle.project_name}/configure')
    yield page
    page.get_by_text("Save").click()
    page.get_by_text("Delete Project").click()
    page.get_by_text("Yes").click()