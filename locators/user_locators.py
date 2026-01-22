from locators.base_locators import BaseLocators


class UserLocators(BaseLocators):
    CREATED_USER_LOC = lambda self, name: f"td > a[href='user/{name}/']"
    DELETE_USER = lambda self, name: f"a[data-url='user/{name.lower()}/doDelete']"
    CONFIRM_DELETE_USER = "button[data-id= 'ok']"