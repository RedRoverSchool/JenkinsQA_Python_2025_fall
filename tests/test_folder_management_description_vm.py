"""
TC_21.010.002 | Folder Management > Add a Job Description > Verify Add folder description #134
----------------------------------------------------------------------------------------------
QA: Vitaly Miller
"""
from playwright.sync_api import expect

#-----------------------------------------------------------------------------------------------------------------------
def test_fill_description(page):
    """
    ---------------------------------------------------
    - 🔑User Authorization (auto)
    - ✏️Заполнение поля Description
    - ✔ Проверка появления текста в заголовке страницы
    - 🧹Очистка поля Description после теста
    - ✔ Проверка отчистки
    ---------------------------------------------------
    """ # <-info
    page.goto('/')                                             # --> Main page (Dashboard) http://localhost:8080/

    # Data
    description_text = 'My test description text!'             # My text

    # Selectors
    add_description_btn = 'a[id="description-link"]'
    description_textura = 'textarea[name="description"]'
    save_btn = 'button[name="Submit"]'
    description_title = 'div[id="description-content"]'

    # Actions
    page.locator(add_description_btn).click()
    page.locator(description_textura).fill(description_text)   # ⚠ Предварительная отчистка поля не требуется. (Переписывает поверх старого)
    page.locator(save_btn).click()

    # Objects
    description_title = page.locator(description_title)

# ✔ Expectations (fill)
    # Проверка появления текста в заголовке
    expect(description_title, '❌Incorrect description text!').to_contain_text(description_text)


# 🧹Очистка поля после теста ----------------
    # Actions
    page.locator(add_description_btn).click()
    page.locator(description_textura).clear()
    page.locator(save_btn).click()

# ✔ Expectations (delete)
    # Проверка, что поле пустое
    expect(description_title, '❌Description is NOT deleted').to_contain_text('')

#-----------------------------------------------------------------------------------------------------------------------
