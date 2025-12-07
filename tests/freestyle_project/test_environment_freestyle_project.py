import pytest
from playwright.sync_api import expect

from tests.freestyle_project.freestyle_data import Freestyle


def test_visible_environment_menu(freestyle):
    environment_menu = freestyle.locator('button[data-section-id="environment"]')

    expect(environment_menu).to_be_visible()

def test_checkboxes_can_be_selected(freestyle):
    build_steps_to_scroll = freestyle.locator('#build-steps')
    checkboxes = freestyle.locator('#environment ~ .jenkins-form-item')
    checkbox_loc = '.row-set-start>.jenkins-checkbox-help-wrapper>.jenkins-checkbox'
    checkbox_check_loc = checkbox_loc + ' input[type="checkbox"]'

    build_steps_to_scroll.scroll_into_view_if_needed()
    count = checkboxes.count()

    for i in range(count):

        expect(checkboxes.nth(i).locator(checkbox_check_loc)).not_to_be_checked()

        checkboxes.nth(i).locator(checkbox_loc).click()

        expect(checkboxes.nth(i).locator(checkbox_check_loc)).to_be_checked()

        checkboxes.nth(i).locator(checkbox_loc).click()

        expect(checkboxes.nth(i).locator(checkbox_check_loc)).not_to_be_checked()

@pytest.mark.parametrize('tp_link, tippy, tp_expected_text', Freestyle.tooltip_environment)
def test_environment_tooltips(freestyle, tp_link, tippy, tp_expected_text) :
    checkboxes = freestyle.locator('#environment ~ .jenkins-form-item')
    checkbox_loc = '.row-set-start>.jenkins-checkbox-help-wrapper>.jenkins-checkbox'

    for i in (0,4) :
        checkboxes.nth(i).locator(checkbox_loc).click()
    checkboxes.nth(0).get_by_text("Advanced").click()
    freestyle.locator(tp_link).hover()
    tp_text = freestyle.locator(f'div#{tippy}')

    expect(tp_text).to_have_text(tp_expected_text)