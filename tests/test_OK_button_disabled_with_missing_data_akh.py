import random

from playwright.sync_api import expect
import time


def test_tc_01_003_08(page):
    page.goto('/')

    new_item_name = f'arkh-{random.randint(1, 9999)}'

    new_item_name_btn_loc = 'a[href="/view/all/newJob"]'
    new_item_field_loc = 'input[id="name"]'
    ok_button_loc = 'button[id="ok-button"]'
    item_type_text = 'Pipeline'
    logo_loc = 'img[src="/static/c4905107/images/svgs/logo.svg"]'
    copy_from_another_item_name_loc = 'input[id="from"]'
    dropdown_loc = 'div.jenkins-dropdown.jenkins-dropdown--compact'

    page.locator(new_item_name_btn_loc).click()

    page.locator(new_item_field_loc).fill(new_item_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_button_loc).click()

    page.locator(logo_loc).click()

    page.locator(new_item_name_btn_loc).click()

    page.locator(new_item_field_loc).fill(new_item_name)

    ok_btn = page.locator("button[id='ok-button']")
    expect(ok_btn).to_be_disabled()

    page.locator(new_item_field_loc).fill('')
    page.locator(copy_from_another_item_name_loc).fill('arkh')


    page.locator(dropdown_loc).wait_for(state="visible")

    page.locator(dropdown_loc).first.click()

    ok_btn = page.locator("button[id='ok-button']")
    expect(ok_btn).to_be_disabled()

    page.locator(copy_from_another_item_name_loc).fill('')
    page.locator(copy_from_another_item_name_loc).fill(new_item_name)

    ok_btn = page.locator("button[id='ok-button']")
    expect(ok_btn).to_be_disabled()



    time.sleep(5)

