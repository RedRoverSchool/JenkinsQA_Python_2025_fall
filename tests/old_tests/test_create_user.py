from playwright.sync_api import expect
import re


class UsersPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("/securityRealm/")

    def open_create_user(self):
        self.page.click("a[href='addUser']")


class CreateUserPage:
    def __init__(self, page):
        self.page = page

    def fill_form(self, username, password, full_name, email):
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password1']", password)
        self.page.fill("input[name='password2']", password)
        self.page.fill("input[name='fullname']", full_name)
        self.page.fill("input[name='email']", email)

    def submit(self):
        self.page.click("button[name='Submit']")


def test_create_user(page):
    users_page = UsersPage(page)
    create_user_page = CreateUserPage(page)

    users_page.open()
    users_page.open_create_user()

    create_user_page.fill_form(
        username="T1im2",
        password="T2i3m4",
        full_name="T1m Sa1go2v",
        email="tim12@sagov.com"
    )

    create_user_page.submit()

    expect(page).to_have_url(re.compile(r"/securityRealm/"))
