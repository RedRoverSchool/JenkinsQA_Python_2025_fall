from playwright.sync_api import expect

def test_AT_15_001_02(page):

    create_user_loc = "a[href='addUser']"
    username_loc = "input[id = 'username']"
    password_loc = "input[name = 'password1']"
    confirm_password_loc = "input[name = 'password2']"
    full_name_loc = "input[name = 'fullname']"
    email_address_loc = "input[name = 'email']"
    create_user_button_loc = "button[name = 'Submit']"

    username = "admin2"
    password = "admin2"
    fullname = "Brown Smith"
    email_address = ""

    page.goto("/securityRealm")

    page.locator(create_user_loc).click()
    page.locator(username_loc).fill(username)
    page.locator(password_loc).fill(password)
    page.locator(confirm_password_loc).fill(password)
    page.locator(full_name_loc).fill(fullname)
    page.locator(email_address_loc).fill(email_address)
    page.locator(create_user_button_loc).click()

    error_message = 'Invalid e-mail address'
    error_loc = page.locator("#main-panel")
    expect(error_loc).to_contain_text(error_message)


