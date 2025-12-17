class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def wait_for_visible(self, locator, timeout: int = 5000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def go_to_project_page(self, name):
        self.page.goto(f"/job/{name}/")

    def clear(self, locator: str):
        self.page.locator(locator).clear()