import random

from playwright.sync_api import expect


def test_tc_01_002_01_create_new_folder(page, new_folder):
    current_url = page.url
    assert new_folder in current_url

    assert new_folder.startswith("Test_folder_")
