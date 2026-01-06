import os
import time

import pytest
from playwright.sync_api import Playwright, ViewportSize
from dotenv import load_dotenv

def test_empty_field(page):
    page.goto("/")
    new_item_link_loc = "a[href='/view/all/newJob']"
    page.locator(new_item_link_loc).click()
    page.get_by_text("Folder", exact=True).click()
    time.sleep(4)
    locator_error = "div[id='itemname-required']"

    assert page.locator(locator_error).inner_text() =="» This field cannot be empty, please enter a valid name"



