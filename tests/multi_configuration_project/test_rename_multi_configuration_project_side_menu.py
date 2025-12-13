from playwright.sync_api import expect


def test_delete_multi_configuration_project_dropdown_side_menu(page, create_multi_conf_project):
    project_name = create_multi_conf_project
    new_project_name = f"New_{project_name}"
    projects_names_loc = "//tr[@id]//a//span"

    page.get_by_role("link", name=f"{project_name}", exact=True).click()

    page.get_by_role("link", name="Rename").click()
    page.locator("input[name='newName']").fill(new_project_name)
    page.get_by_role("button", name="Rename").click()

    page.goto("/")
    expect(page.get_by_text(project_name, exact=True)).not_to_be_visible()
    expect(page.locator(projects_names_loc).filter(has_text=new_project_name)).to_be_visible()





