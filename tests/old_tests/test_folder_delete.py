from playwright.sync_api import expect

def test_folder_delete(page):
    page.goto("/")

    folder_name = "Tim"

    # Click "New Item"
    page.locator("a[href='/view/all/newJob']").click()

    # Enter folder name
    page.locator("#name").fill(folder_name)

    # Select Folder type (the correct one)
    page.locator("li.com_cloudbees_hudson_plugins_folder_Folder").click()

    # Click OK
    page.locator("#ok-button").click()

    # Go back to Dashboard
    page.locator("a[href='/']").click()

    # Make sure folder exists before deleting
    expect(page.get_by_role("link", name=folder_name, exact=True)).to_be_visible()

    # Delete folder
    # Open dropdown for this specific folder row
    page.locator(f"tr:has-text('{folder_name}') .jenkins-menu-dropdown-chevron").click(force=True)

    # Click "Delete" inside dropdown
    page.locator(f"button[href*='/job/{folder_name}/doDelete']").click()

    # Confirm deletion
    page.locator("button[data-id='ok']").click()

    # Expected Result: folder is deleted
    expect(page.get_by_role("link", name=folder_name, exact=True)).not_to_be_visible()