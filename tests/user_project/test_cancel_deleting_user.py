from tests.user_project.conftest import delete_user

def test_tc_15_003_01(page, new_user):

    page.goto("/securityRealm/")

    user_name = new_user

    user_loc = f"td>a[href='user/{user_name}/']"
    delete_user_loc = "svg.icon-edit-delete"
    cancel_button_loc = "button[data-id='cancel']"

    page.locator(user_loc).click()
    page.click(delete_user_loc)
    page.click(cancel_button_loc)

    page.goto("/securityRealm/")

    user_count = page.get_by_text(user_name).count()
    assert user_count == 1, f"Пользователь {user_name}  не найден "
    if user_count == 1:
        print(f" Отмена удаления пользователя, {user_name} остался в системе")
    """Удаление пользователя после теста"""

    delete_user(page,user_name)

