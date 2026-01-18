from utils.generators.project_generator import ProjectGenerator
from pages.new_item_page import NewItemPage
from locators.new_item_locators import NewItemLocators


class TestUniqueItemName:

    def setup_unique_item_name(self, create_job):
        folder_name = ProjectGenerator.generate_folder_name()
        freestyle_name = ProjectGenerator.generate_freestyle_name()

        create_job(name=folder_name, job_type="folder")
        create_job(name=freestyle_name, job_type="freestyle", folder=folder_name)

        return folder_name, freestyle_name

    def attempt_duplicate_creation(self, open_page, folder_name, freestyle_name):
        duplicate_page = open_page(NewItemPage, f"/job/{folder_name}/newJob")
        duplicate_page.fill(NewItemLocators.NAME_FIELD, freestyle_name)

        return duplicate_page