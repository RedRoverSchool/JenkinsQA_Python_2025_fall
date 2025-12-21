from locators.base_locators import BaseLocators


class UserLocators(BaseLocators):
    CREATED_USER_LOC = lambda self, name: f"td > a[href='user/{name}/']"