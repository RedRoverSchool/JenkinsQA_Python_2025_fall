class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def get_all_texts(self, locator: str, text=None) -> str:
        return self.page.locator(locator, has_text=text).all_inner_texts()

    def wait_for_visible(self, locator, timeout: int = 5000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def go_to_project_page(self, name):
        self.page.goto(f"/job/{name}/")

    def clear(self, locator: str):
        self.page.locator(locator).clear()