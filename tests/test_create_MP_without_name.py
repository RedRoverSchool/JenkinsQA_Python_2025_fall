from playwright.sync_api import sync_playwright, expect

# Основной URL, который будет использоваться для всех относительных путей
BASE_URL = "http://localhost:8080"

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Устанавливаем базовый URL для всех переходов
        page.goto(f"{BASE_URL}/login")  # Переход на страницу логина

        page.locator("#j_username").fill("DariaIa")
        page.locator("input[name='j_password']").fill("Assistants89!")
        page.locator("button[name='Submit']").click()

        # Ждём редиректа на главную страницу, используя относительный путь
        page.wait_for_url(f"{BASE_URL}/")

        # Проверка успешного логина: выбираем только первый элемент с текстом 'All'
        expect(page.locator("a:has-text('All')").first).to_be_visible(timeout=5000)
        browser.close()