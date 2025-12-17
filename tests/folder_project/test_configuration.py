from data.enums import ItemType


class TestConfiguration:
    FOLDER_NAME = "folder"
    DESCRIPTION = "Lorem ipsum and bla bla bla bla and etc"

    def test_apply_configuration(self,create_job, base_configuration_page, base_project_page):
        '''TC_05.004.01 | Folder Configuration > Save or Apply> Apply configuration'''

        create_job(self.FOLDER_NAME, ItemType.FOLDER)
        base_configuration_page.go_to_configuration_page(self.FOLDER_NAME)
        base_configuration_page.set_or_change_description(self.DESCRIPTION)
        base_configuration_page.apply_changes()
        base_configuration_page.go_to_project_page(self.FOLDER_NAME)

        assert base_project_page.description_text() == self.DESCRIPTION