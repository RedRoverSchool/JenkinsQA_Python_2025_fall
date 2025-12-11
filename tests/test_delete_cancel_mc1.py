from playwright.sync_api import expect

def test_delete_cancel_mc1(page):
    page.goto("/")

    job_row = page.locator("tr:has-text('MC1')")

    job_row.locator(".jenkins-menu-dropdown-chevron").click(force=True)

    page.locator("button[href='/job/MC1/doDelete']").click()

    page.locator("button[data-id='cancel']").click()

    expect(page).to_have_url("/")