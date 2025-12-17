from data.enums import ItemType


class TestConfiguration:

    def test_apply_configuration(self,create_job, base_configuration_page, base_project_page):
        '''TC_05.004.01 | Folder Configuration > Save or Apply> Apply configuration'''
        FOLDER_NAME = "folder"
        DESCRIPTION = "Lorem ipsum and bla bla bla bla and etc"

        create_job(FOLDER_NAME, ItemType.FOLDER)
        base_configuration_page.go_to_configuration_page(FOLDER_NAME)
        base_configuration_page.set_or_change_description(DESCRIPTION)
        base_configuration_page.apply_changes()
        base_configuration_page.go_to_project_page(FOLDER_NAME)

        assert base_project_page.description_text() == DESCRIPTION