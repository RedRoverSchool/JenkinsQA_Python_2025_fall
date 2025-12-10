import random
from time import sleep

from playwright.sync_api import Playwright, sync_playwright, expect

def test_cancel_delete_from_page_project(page):
    page.goto("/")
    new_freestyle_project_name = f"freestyle-{random.randint(1, 9999)}"
    freestyle_btn_loc = '#job_freestyle-6115 > td:nth-child(3) > a'

    new_item_btn_loc = 'a[href="/view/all/newJob"]'
    item_name_field_loc = 'input[class="jenkins-input"]'
    item_type_text = "Freestyle project"
    ok_btn_loc = 'button[id="ok-button"]'
    logo_loc = 'img[id="jenkins-head-icon"]'
    # created_item_loc = lambda name: f"td > a[href='job/{name}/']"

    """Страница добавления item"""
    page.locator(new_item_btn_loc).click()
    page.locator(item_name_field_loc).fill(new_freestyle_project_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn_loc).click()
    """Возвращение на главную"""
    page.locator(logo_loc).click()
    page.locator(freestyle_btn_loc).click()
    sleep(1)
    page.get_by_role("link", name="Delete Project").click()
    page.get_by_role("button", name="Cancel").click()
    page.locator(logo_loc).click()

    assert page.locator(freestyle_btn_loc).is_visible()


