import random

import pytest


@pytest.fixture()
def new_user(page):

    username = f"test_user_{random.randint(0, 9999999)}"
    password = f"test_password_{random.randint(0, 9999999)}"
    full_name = f"test_full_name_{random.randint(0, 9999999)}"
    email = f"test_email_{random.randint(0, 9999999)}@example.com"


    page.goto("/")

    user_settings_btn_loc = "a[id='root-action-ManageJenkinsAction']"

    users_settings_btn_loc = "a[href='securityRealm/']"
    create_user_btn_loc = "a[href='addUser']"

    create_username_loc = "input[id='username']"
    create_password_loc = "input[name='password1']"
    create_confirm_password_loc = "input[name='password2']"
    create_full_name_loc = "input[name='fullname']"
    create_email_loc = "input[name='email']"
    create_btn_loc = "button[formnovalidate='formNoValidate']"
    created_user_loc = lambda name: f"td > a[href='user/{username}/']"

    page.locator(user_settings_btn_loc).click()
    page.locator(users_settings_btn_loc).click()
    page.locator(create_user_btn_loc).click()

    page.locator(create_username_loc).fill(username)
    page.locator(create_password_loc).fill(password)
    page.locator(create_confirm_password_loc).fill(password)
    page.locator(create_full_name_loc).fill(full_name)
    page.locator(create_email_loc).fill(email)
    page.locator(create_btn_loc).click()
    username = page.locator(created_user_loc(username)).text_content()
    #assert text == username
    return username

"""удаление созданного пользователя"""
def delete_user(page,name):

    user_loc = f"td>a[href='user/{name}/']"
    delete_user_loc = "svg.icon-edit-delete"
    ok_button_loc = "button[data-id='ok']"

    page.locator(user_loc).click()
    page.click(delete_user_loc)
    page.click(ok_button_loc)

