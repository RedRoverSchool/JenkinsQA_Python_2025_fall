from playwright.sync_api import expect

def test_tc_11_001_02(page):
    page.goto("/")

    create_job_btn = page.locator('[href="newJob"]')
    create_job_btn.click()

    new_page = page.locator("#add-item-panel").get_by_text('New Item')
    expected_url = "http://localhost:8080/newJob"

    expect(page).to_have_url(expected_url)
    expect(new_page).to_be_visible()