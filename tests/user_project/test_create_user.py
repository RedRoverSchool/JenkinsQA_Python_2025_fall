import time

from data.endpoints import Endpoints
from locators.user_locators import UserLocators
from pages.user_page import UserPage


class TestCreateUser:
    locators = UserLocators()
    endpoints = Endpoints()

    def test_tc_15_001_04_delete_user(self, create_user_fixture, open_page):
        username = create_user_fixture.username
        user_page = open_page(UserPage, self.endpoints.SECURITY_REALM_URL)
        user_page.delete_user(username)
        text = user_page.get_user_name(username)

        assert text == "User not exists"


