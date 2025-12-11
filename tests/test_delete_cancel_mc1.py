from playwright.sync_api import expect

def test_delete_cancel_mc1(page):
    page.goto("/")

    row = page.locator("tbody tr").filter(has_text="MC1")
    expect(row).to_be_visible()

    dropdown = row.locator(".jenkins-menu-dropdown-chevron")
    expect(dropdown).to_be_visible()
    dropdown.click(force=True)

    delete_btn = page.get_by_text("Delete Multi-configuration project", exact=True)
    expect(delete_btn).to_be_visible()
    delete_btn.click()

    cancel_btn = page.locator("button[data-id='cancel']")
    expect(cancel_btn).to_be_visible()
    cancel_btn.click()

    expect(page).to_have_url("/")