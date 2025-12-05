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