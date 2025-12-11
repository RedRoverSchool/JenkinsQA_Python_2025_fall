from playwright.sync_api import expect


def test_delete_cancel_mc1(page):
    page.goto("/")

    page.locator(
        "button.jenkins-menu-dropdown-chevron[data-href*='/job/MC1/']"
    ).click(force=True)

    page.locator(
        "button.jenkins-dropdown__item[href='/job/MC1/doDelete']"
    ).click()

    page.locator("button[data-id='cancel']").click()

    expect(page).to_have_url("/")