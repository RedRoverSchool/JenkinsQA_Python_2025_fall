import time

from data.endpoints import Endpoints
from locators.user_locators import UserLocators
from pages.user_page import UserPage


class TestUser:
    locators = UserLocators()
    endpoints = Endpoints()

    def test_denis(self, create_user_fixture, open_page):
        username = create_user_fixture.username
        user_page = open_page(UserPage, f"{self.endpoints.MANAGE_URL}{self.endpoints.SECURITY_REALM_URL}")
        text = user_page.get_text(self.locators.CREATED_USER_LOC(username))
        time.sleep(1)
        assert text == username