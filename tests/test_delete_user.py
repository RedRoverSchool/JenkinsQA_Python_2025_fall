import random


def test_tc_15_003_06(page):

    username = "User1"
    password = f"test_password_{random.randint(0, 9999999)}"
    full_name = f"test_full_name_{random.randint(0, 9999999)}"
    email = f"test_email_{random.randint(0, 9999999)}@example.com"

    page.goto("/manage/securityRealm/")

    create_user_btn_loc = "a[href='addUser']"
    username_field_loc = "input[id='username']"
    password_field_loc = "input[name='password1']"
    confirm_password_field_loc = "input[name='password2']"
    full_name_field_loc = "input[name='fullname']"
    email_field_loc = "input[name='email']"
    create_btn_loc = "button[formnovalidate='formNoValidate']"
    created_user_loc = lambda name: f"td > a[href='user/{username.lower()}/']"
    delete_user_btn_loc = "a[data-url='user/user1/doDelete']"
    ok_btn_loc = "button[data-id='ok']"

    page.locator(create_user_btn_loc).click()
    page.locator(username_field_loc).fill(username)
    page.locator(password_field_loc).fill(password)
    page.locator( confirm_password_field_loc).fill(password)
    page.locator(full_name_field_loc).fill(full_name)
    page.locator(email_field_loc).fill(email)
    page.locator(create_btn_loc).click()

    text = page.locator(created_user_loc(username)).text_content()
    assert text == username

    page.locator(delete_user_btn_loc).click()
    page.locator(ok_btn_loc).click()

    assert username not in page.content()

















