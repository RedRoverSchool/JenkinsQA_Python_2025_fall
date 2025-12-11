import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_ok_button_login():
    browser = None
    try:
        async with async_playwright() as p:

            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()


            await page.goto("http://localhost:8080/login")


            ok_button = page.locator("[name='Submit']")
            username_input = page.locator("#j_username")
            password_input = page.locator("[name='j_password']")


            await expect(ok_button).to_be_visible()
            assert await ok_button.is_enabled(), "Кнопка должна быть включена изначально"


            await username_input.fill("DariaIa")
            await password_input.fill("Solutions89!")


            assert await ok_button.is_enabled(), "Кнопка должна оставаться включенной после ввода"

    except Exception as e:

        if browser:
            page = await browser.new_page()
            await page.screenshot(path="error_screenshot.png")
        raise e
    finally:
        if browser:
            await browser.close()