from playwright.sync_api import expect

def test_delete_cancel_mc1(page):
    page.goto("/")

    page.locator("button[aria-expanded='false']").first.click(force=True)

    delete_btn = page.locator(
        "button.jenkins-dropdown__item[href='/job/MC1/doDelete']"
    )
    delete_btn.click()

    cancel_btn = page.locator("button[data-id='cancel']")
    cancel_btn.click()

    expect(page).to_have_url("/")