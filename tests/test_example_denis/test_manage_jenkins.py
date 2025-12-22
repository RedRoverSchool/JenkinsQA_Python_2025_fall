import time

import pytest

from conftest import open_page
from data.data import ManageJenkinsData
from data.endpoints import Endpoints
from pages.manage_page import ManageJenkinsPage
from utils.assertions import Assertions


class TestVisibilityAndClickability:
    data = ManageJenkinsData()
    assertions = Assertions()
    endpoints = Endpoints()

    @pytest.mark.parametrize("name", data.STATUS_INFORMATION)
    def test_status_information_block_buttons(self, open_page, name):
        manage_page = open_page(ManageJenkinsPage, self.endpoints.MANAGE_URL)
        text = manage_page.asd(name)
        self.assertions.assert_text(name, text)
