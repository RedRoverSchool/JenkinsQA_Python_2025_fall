from playwright.sync_api import expect


def test_delete_multi_configuration_project_dropdown(page, create_multi_conf_project):
    project_name = create_multi_conf_project
    project_link = page.get_by_role("link", name=f"{project_name}", exact=True)

    project_link.hover()
    project_link.get_by_role("button").click(force=True)
    page.get_by_text("Delete Multi-configuration project").click()
    page.get_by_role("button", name="Yes", exact=True).click()

    expect(page).to_have_url("/")
    expect(page.get_by_text(project_name, exact=True)).not_to_be_visible()


