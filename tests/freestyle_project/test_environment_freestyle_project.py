from playwright.sync_api import expect


def test_visible_environment_menu(freestyle):
    environment_menu = freestyle.locator('button[data-section-id="environment"]')

    expect(environment_menu).to_be_visible()