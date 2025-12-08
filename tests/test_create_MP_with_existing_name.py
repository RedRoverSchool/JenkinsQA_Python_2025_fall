import random
import string



def test_tc_01_005_05(page):
    """локатор кнопки new item"""
    new_item_loc = "a[href='/view/all/newJob']"
    """Локатор кнопки Multibranch pipeline"""
    pipeline_multi_loc = "Freestyle project"
    """Локатор сообщения о занятом имени"""
    message_loc = "div[id='itemname-invalid']"
    """Текст сообщения об ошибке"""
    message = "» A job already exists with the name ‘test’"
    field_name_loc = "input[name='name']"
    button_ok_loc = "button[id='ok-button']"
    jenkins_logo_loc = "img[id='jenkins-head-icon']"


    """Случайное имя нового айтема"""
    name_item = ''.join(random.choices(string.ascii_lowercase, k=5))

    page.goto("/")
    page.locator(new_item_loc).click()
    page.locator(field_name_loc).fill(name_item)
    page.get_by_text(pipeline_multi_loc).click()
    page.locator(button_ok_loc).click()
    page.locator(jenkins_logo_loc).click()

    created_item_loc = lambda name: f"td > a[href='job/{name}/']"
    new_item_name = page.locator(created_item_loc(name_item)).text_content()
    """Повторное создание айтема с использованным именем"""
    page.locator(new_item_loc).click()
    page.locator(field_name_loc).fill(new_item_name)

    """Проверка, что текст сообщения об ошибке появляется на странице"""
    assert new_item_name == name_item

