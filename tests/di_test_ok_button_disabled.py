import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_ok_button_login():
    # Асинхронный контекст Playwright прямо в тесте
    async with async_playwright() as p:
        # Запускаем браузер в headless режиме
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Переходим на страницу логина Jenkins
        await page.goto("http://localhost:8080/login")

        # Локаторы
        ok_button = page.locator("[name='Submit']")
        username_input = page.locator("#j_username")
        password_input = page.locator("[name='j_password']")

        # Проверяем, что кнопка видима и включена
        await expect(ok_button).to_be_visible()
        assert await ok_button.is_enabled(), "Кнопка должна быть включена изначально"

        # Вводим логин и пароль
        await username_input.fill("DariaIa")
        await password_input.fill("Solutions89!")

        # Проверяем, что кнопка остаётся включенной после ввода
        assert await ok_button.is_enabled(), "Кнопка должна оставаться включенной после ввода"

        # Закрываем браузер
        await browser.close()








