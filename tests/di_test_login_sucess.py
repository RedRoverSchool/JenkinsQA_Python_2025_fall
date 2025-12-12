import pytest
from playwright.async_api import async_playwright, expect

JENKINS_URL = "http://localhost:8080/login"
USERNAME = "DariaIa"
PASSWORD = "Solutions89!"

@pytest.mark.asyncio
async def test_jenkins_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # 1. Переход на страницу логина
        await page.goto(JENKINS_URL)

        # 2. Заполнение формы логина
        await page.fill("#j_username", USERNAME)
        await page.fill("input[name='j_password']", PASSWORD)
        await page.click("input[name='Submit']")

        # 3. Скриншот после клика (для дебага)
        await page.screenshot(path="after_login.png")

        # 4. Ждём появления Dashboard
        dashboard_locator = page.locator("#main-panel")  # основной контейнер Dashboard
        await dashboard_locator.wait_for(state="visible", timeout=20000)

        # 5. Проверка, что Dashboard действительно виден
        assert await dashboard_locator.is_visible(), "Dashboard не отображается!"

        print("Login successful, Dashboard visible!")

        await browser.close()
