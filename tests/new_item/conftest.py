import pytest

@pytest.fixture()
def open_main_page(page):
    page.goto("/")


@pytest.fixture(scope="function", autouse=True)
def delete_jobs_after_all_tests():
    yield