from playwright.sync_api import expect


def test_tc_11_003_01_manage_jenkins_page(page):

    manage_jenkins_label_loc = "text=Manage Jenkins"
    expected_sections = [
        "System Configuration",
        "Security",
        "Status Information",
        "Troubleshooting",
        "Tools and Actions"
    ]
    page.goto("/")
    page.locator(manage_jenkins_label_loc).click()

    expect(page).to_have_url("http://localhost:8080/manage/")

    for section in expected_sections:
       sections_loc = page.get_by_role("heading", name=section)
       expect(sections_loc).to_be_visible()
