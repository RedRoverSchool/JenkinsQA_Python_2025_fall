from data.enums import ItemType


class TestConfigurationDuplicate:
    NAME_FOLDER = "smoke_test1"
    DESCRIPTION = "KAK KAK KAK"

    def test_configuration_duplicate(self, create_job, base_configuration_page, page, base_project_page):

        create_job(self.NAME_FOLDER ,ItemType.FOLDER )
        base_configuration_page.go_to_configuration_page(self.NAME_FOLDER)
        base_configuration_page.set_or_change_description(self.DESCRIPTION)
        base_configuration_page.save_configuration()
        text_description = base_project_page.description_text(self.DESCRIPTION)

        assert text_description == self.DESCRIPTION
