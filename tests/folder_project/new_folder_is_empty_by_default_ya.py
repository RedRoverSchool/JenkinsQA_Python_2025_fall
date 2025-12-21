from playwright.sync_api import expect
from data.enums import ItemType
from utils.generators.project_generator import ProjectGenerator

def test_tc_01_002_04_new_folder_is_empty_by_default(create_job, base_project_page):
    """TC_01.002.04 | New Item > Folder > Verify a new folder is empty by default"""

    folder_name = ProjectGenerator.generate_folder_name()
    create_job(folder_name, ItemType.FOLDER)
    base_project_page.go_to_project_page(folder_name)

    expect(base_project_page.page.get_by_text("This folder is empty")).to_be_visible()





