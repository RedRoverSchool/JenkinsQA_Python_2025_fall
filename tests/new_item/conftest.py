import pytest


@pytest.fixture(scope="function", autouse=True)
def delete_jobs_after_all_tests():
    yield