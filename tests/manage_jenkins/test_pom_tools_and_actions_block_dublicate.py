import pytest
from data.data import ManageJenkinsData
from data.endpoints import Endpoints
from pages.manage_page import ManageJenkinsPage
from utils.assertions import Assertions


class TestToolsAndActionsBlockDublicate:
    endpoints = Endpoints()
    data = ManageJenkinsData()
    assertions = Assertions()

    @pytest.mark.parametrize("name", data.TOOLS_AND_ACTIONS)
    def test_tools_and_actions_block_content(self, open_page, name):
        manage_page = open_page(
            ManageJenkinsPage,
            self.endpoints.MANAGE_URL
        )

        text = manage_page.get_tools_and_actions_item_text(name)
        self.assertions.assert_text(name, text)